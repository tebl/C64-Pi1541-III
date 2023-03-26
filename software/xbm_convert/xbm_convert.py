#
# Converts XBM-files created using Gimp. The Pi1541 softwares format used for
# images is directly linked to the memory orientation of the display being
# used, meaning that for standard 128x64 OLED displays we need to reorient the
# pixels so that they are stored vertically.
#
import sys
from argparse import ArgumentParser
from glob import glob
from os import path

WIDTH = 128
HEIGHT = 64
PIXEL_SET = ' '
PIXEL_OFF = '#'

class ImageMap:
    def __init__(self, bytes, width, height):
        self.width = width
        self.height = height
        self.data = [0]*(width*height)

        pos = 0
        for byte in bytes:
            bits = (bin(byte)[2:]).zfill(9)[::-1]
            for i in range(0,8):
                self.data[pos] = bits[i]
                pos += 1


    def get_pixel(self, x, y):
        return self.data[(y * self.width) + (x % self.width)]


    def print(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.get_pixel(x, y) == '1':
                    print(PIXEL_SET, end='')
                else:
                    print(PIXEL_OFF, end='')
            print()


    def get_byte_horizontal(self, x, y):
        bits = []
        for i in range(0, 8):
            bits.append(self.get_pixel(x + i, y))
        bits = ''.join(bits)[::-1]
        return int(bits, 2)

    
    def get_bytes_horizontal(self):
        bytes = []
        for y in range(0, self.height):
            for x in range(0, self.width, 8):
                bytes.append(self.get_byte_horizontal(x, y))
        return bytearray(bytes)


    def get_byte_vertical(self, x, y):
        bits = []
        for i in range(0, 8):
            bits.append(self.get_pixel(x, y + i))
        bits = ''.join(bits)[::-1]
        bits = ''.join('1' if x == '0' else '0' for x in bits)
        return int(bits, 2)

    
    def get_bytes_vertical(self):
        bytes = []
        for y in range(0, self.height, 8):
            for x in range(0, self.width):
                bytes.append(self.get_byte_vertical(x, y))
        return bytearray(bytes)


    def get_bytes(self, pixel_orientation):
        if pixel_orientation == 'vertical':
            return self.get_bytes_vertical()
        elif pixel_orientation == 'horizontal':
            return self.get_bytes_horizontal()
        else:
            raise ValueException('Pixel orientation "' + pixel_orientation + '" unknown')


    def write(self, path_out, pixel_orientation):
        output = open(path_out, 'wb')
        bytes = self.get_bytes(pixel_orientation)
        output.write(bytes)
        output.close()


def convert_file(path_in, path_out, pixel_orientation='vertical'):
    print("-", path_in, ">>", path_out)
    input = open(path_in, 'r')

    found = False
    while True:
        char = input.read(1)
        if char == '{':
            found = True
            break

    if found:
        lines = input.read()
        lines = lines.replace('0x','')
        lines = lines.replace(',','')
        lines = lines.replace(' ','')
        lines = lines.replace('}','')
        lines = lines.replace(';','')
        lines = lines.replace('\n','')
        lines = lines.replace('\r','')

        bytes = bytearray.fromhex(lines)
        map = ImageMap(bytes, WIDTH, HEIGHT)
        map.write(path_out, pixel_orientation)   
    input.close()


def show_file(path_in):
    input = open(path_in, 'r')

    found = False
    while True:
        char = input.read(1)
        if char == '{':
            found = True
            break

    if found:
        lines = input.read()
        lines = lines.replace('0x','')
        lines = lines.replace(',','')
        lines = lines.replace(' ','')
        lines = lines.replace('}','')
        lines = lines.replace(';','')
        lines = lines.replace('\n','')
        lines = lines.replace('\r','')

        bytes = bytearray.fromhex(lines)
        map = ImageMap(bytes, WIDTH, HEIGHT)
        map.print()
    input.close()    


def parse_arguments():
    '''
    Parses command line arguments and runs the appropriate tasks.
    '''
    help_text = '''
    Simple tool created for use with Pi1541s with 128x64 OLED displays
    installed, while the format is a simple monochrome image with 1-bit
    representing a single pixel (8 pixels packed into a single byte).
    The XBM-file format is supported by Gimp and can be edited as such,
    but not in the form that we need - this script takes care of fixing
    that by storing the pixels vertically instead of the normal
    horizontal orientation.
    '''
    parser = ArgumentParser(description=help_text)
    parser.add_argument('-a', '--all', help='Convert all XBM-files', action='store_true')
    parser.add_argument('-c', '--convert', help='Convert specified XBM-file', nargs='*', default=[])
    parser.add_argument('-s', '--show', help='Show approximation of XBM-file (using characters so you need a wide terminal)', nargs='*', default=[])
    parser.add_argument('-p', '--pixel-order', help='Specify how to store the pixels, vertical as used by Pi1541 - or you can keep them horizontal', default='vertical', choices=['vertical', 'horizontal'])
    parser.add_argument('-v', '--version', action='version', version='XBM Converter 1.0')
    args = parser.parse_args()

    errors = False
    if not errors:
        for path_in in args.convert:
            try:
                if not path.isfile(path_in):
                    print("Error converting {0} ({1})".format(path_in, 'no such file'))
                convert_file(path_in, path_in.removesuffix(".xbm") + ".raw", args.pixel_order)
            except Exception as err:
                errors = True
                print("Uncaught exception converting {0} ({1})".format(path_in, err))
                break

    if not errors:
        for path_in in args.show:
            try:
                if not path.isfile(path_in):
                    print("Error displaying {0} ({1})".format(path_in, 'no such file'))
                show_file(path_in)
            except Exception as err:
                errors = True
                print("Uncaught exception converting {0} ({1})".format(path_in, err))
                break

    if not errors:
        if args.all:
            print('Converting all XBM-files:')
            for file in glob("*.xbm"):
                convert_file(file, file.removesuffix(".xbm") + ".raw", args.pixel_order)

    print("Done.")

    
if __name__ == "__main__":
    parse_arguments()
