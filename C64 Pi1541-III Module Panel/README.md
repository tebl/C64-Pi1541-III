# Pi1541-III Module Panel
This PCB holds the components for the front panel, it was designed to mount on top of [Pi1541-III Module](https://github.com/tebl/C64-Pi1541-III/tree/main/C64%20Pi1541-III%20Module). This panel has its own BOM, so keep that in mind when ordering components - as you'll be needing parts listed for both of them to build a complete device.

- [1> Build instructions](#1-build-instructions)
- [2> Schematic](#2-schematic)
- [3> BOM](#3-bom)

![Current PCB](https://raw.githubusercontent.com/tebl/C64-Pi1541-III/main/gallery/build_020.jpg)

# 1> Build instructions
Assembling this module is covered as part of the overall documentation, as linked below. Note that *BOM* is supplied per module, the one belonging to this module in particular is included as part of this document (click [here](#3-bom) to go there).
- [Assembling one](https://github.com/tebl/C64-Pi1541-III/blob/main/documentation/assembling_one.md)

# 2> Schematic
The supplied KiCad files should be sufficient as both a schematic and as a  starting point for ordering PCBs (basically you could just zip the contents of the export folder and upload that on a fabrication site), the schematic is also available in [PDF-format](https://github.com/tebl/C64-Pi1541-III/tree/main/documentation/schematic) and this is what you'll need to print and work your way through this things don't work as expected after assembly.

# 3> BOM
Most parts should be easy to get a hold of from your favourite local electronic component shop, but given that I don't have access to such shops where I live so everything was based on whatever I could get cheapest from eBay/AliExpress (free shipping, but plan on waiting 3-4 weeks for delivery). Components in parenthesis can be considered optional for features beyond the more basic functionality, but where's the fun in that? You deserve the complete package.

| Reference             | Item                                                              | Count | Order  |
| --------------------- | ----------------------------------------------------------------- | ----- | ------ |
| Module Panel PCB      | PCB specific to this project                                      |     1 | [See modules](https://github.com/tebl/C64-Pi1541-III/blob/main/README.md#1-modules)
| Faceplate (FP1) PCB   | Front faceplate                                                   |    (1)| [See modules](https://github.com/tebl/C64-Pi1541-III/blob/main/README.md#1-modules)
| IC1 *1                | SH1106 I2C OLED 128x64 (1.3")                                     |     1 |
| ENC1                  | EC11 rotary encoder, 20mm. Preferably plum handle.                |     1 |
|                       | Suitable knob for rotary encoder, max 20mm in diameter.           |    (1)|
| D1,D2                 | 2x5x7mm rectangular LED, suitably coloured.                       |     2 |
| J1                    | 12-pin right-angle pin header                                     |     1 |
| SW1,SW2               | 6x6mm momentary switch, 10.5mm or taller.                         |     2 |
| Mounting *2           | Nylon M3 hex standoffs 8mm (M-F)                                  |     4 |
| Mounting *2           | Nylon M3x6mm nylon screws                                         |     4 |
| Mounting *2           | Nylon M3x6mm nylon nuts                                           |     4 |

1) Many of these will be listed for sale as 1.3" ssd1306-based OLED displays, but they actually have the slightly different sh1106-controller. Something to keep in mind when ordering.
2) These are used in various places of the project, these are available in the form of kits usually advertised *M3 nylon standoff kit* which should contain most of what you'd need though you should check that they include them in sufficient quantity.