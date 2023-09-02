# Pi1541-III Module
This is the main PCB and will hold most of the active components in the device, but note that it is designed to be used with [Pi1541-III Module Panel](https://github.com/tebl/C64-Pi1541-III/tree/main/C64%20Pi1541-III%20Module%20Panel) and has one listed in the [BOM](#3-bom). Note that the mentioned panel also has its own separate [BOM](https://github.com/tebl/C64-Pi1541-III/tree/main/C64%20Pi1541-III%20Module%20Panel/README.md#3-bom), so keep that in mind while ordering components.

- [1> Build instructions](#1-build-instructions)
- [2> Schematic](#2-schematic)
- [3> BOM](#3-bom)

![Current PCB](https://raw.githubusercontent.com/tebl/C64-Pi1541-III/main/gallery/build_002.jpg)

# 1> Build instructions
Assembling this module is covered as part of the overall documentation, as linked below. Note that *BOM* is supplied per module, the one belonging to this module in particular is included as part of this document (click [here](#3-bom) to go there).

- [Assembling one](https://github.com/tebl/C64-Pi1541-III/blob/main/documentation/assembling_one.md)

# 2> Schematic
The supplied KiCad files should be sufficient as both a schematic and as a  starting point for ordering PCBs (basically you could just zip the contents of the export folder and upload that on a fabrication site), the schematic is also available in [PDF-format](https://github.com/tebl/C64-Pi1541-III/tree/main/documentation/schematic) and this is what you'll need to print and work your way through this things don't work as expected after assembly.

# 3> BOM
Most parts should be easy to get a hold of from your favourite local electronic component shop, but given that I don't have access to such shops where I live so everything was based on whatever I could get cheapest from eBay/AliExpress (free shipping, but plan on waiting 3-4 weeks for delivery). Components in parenthesis can be considered optional for features beyond the more basic functionality, but where's the fun in that? You deserve the complete package.

| Reference             | Item                                                              | Count | Order  |
| --------------------- | ----------------------------------------------------------------- | ----- | ------ |
| Module PCB            | PCB specific to this project                                      |     1 | [See modules](https://github.com/tebl/C64-Pi1541-III/blob/main/README.md#1-modules)
| Faceplate (FB1) PCB   | Top faceplate                                                     |     1 | [See modules](https://github.com/tebl/C64-Pi1541-III/blob/main/README.md#1-modules)
| Faceplate (FB2) PCB   | Bottom faceplate                                                  |    (1)| [See modules](https://github.com/tebl/C64-Pi1541-III/blob/main/README.md#1-modules)
| A1                    | 2x20 pin female header                                            |     1 |
|                       | Raspberry Pi version 3B,3B+ or 3A+                                |     1 |
| A2 *1                 | 4ch I2C level converter module                                    |     1 |
| BZ1                   | Passive buzzer (pin spacing from 3.81 to 7mm will work)           |   (1) |
| C1                    | 100nF ceramic capacitor (5mm)                                     |     1 |
| C6                    | 470uF electrolytic capacitor (8mm x 3.5mm)                        |     1 |
| J1                    | 2.1mm x 5.5mm barrel plug                                         |     1 |
| J2,J3                 | Female S-terminal 6-pin DIN PCB                                   |  1 (1)|
| J8                    | [Pi1541-III Module Panel](https://github.com/tebl/C64-Pi1541-III/tree/main/C64%20Pi1541-III%20Module%20Panel) (completed unit) | 1 |
| R1,R2                 | 1k Ohm resistor                                                   |     2 |
| R3,R4                 | 10k Ohm resistor                                                  |     2 |
| R6,R7 *2              | 470 Ohm resistor                                                  |     2 |
| U1 *3                 | 7406 (DIP-14)                                                     |     1 |
| Mounting *4           | Nylon M3 hex standoffs 6mm (M-F)                                  |     4 |
| Mounting *4           | Nylon M3 hex standoffs 8mm (M-F)                                  |     2 |
| Mounting *5           | Nylon M3 hex standoffs 12mm (M-F)                                 |    (4)|
| Mounting *4           | Nylon M3 hex standoffs 20mm (M-F)                                 |     4 |
| Mounting *4           | Nylon M3x6mm nylon screws                                         |     6 |
| Mounting *4           | Nylon M3x6mm nylon nuts                                           |     12 |

1) There are multiple configurations of these being sold, this is usually sold with a blue PCB. When in doubt, compare the sale listing with the one shown in this [image](https://raw.githubusercontent.com/tebl/C64-Pi1541-III/main/gallery/build_006B.jpg).
2) This is the resistor for the LEDs mounted on [Pi1541-III Module Panel](https://github.com/tebl/C64-Pi1541-III/tree/main/C64%20Pi1541-III%20Module%20Panel), the value need to be sized according to the type of LED being used. This value is a somewhat safe choice cheaper coloured LEDs, for anything blue or especially marked as being *bright* - then you need to calculate a proper value for these.
3) There are unfortunately counterfeit 7406-chips being circulated, the ones I've had the most success with has been marked 7406PC though a handful of SN7406 have also been found working. See [troubleshooting](https://github.com/tebl/C64-Pi1541-III/blob/main/documentation/troubleshooting.md) for more information.
4) These are used in various places of the project, these are available in the form of kits usually advertised *M3 nylon standoff kit* which should contain most of what you'd need though you should check that they include them in sufficient quantity.
5) These are only needed when *NOT* installing bottom faceplate ([Pi1541-III Faceplate (FB2)](https://github.com/tebl/C64-Pi1541-III/tree/main/faceplates/C64%20Pi1541-III%20Module%20FB2))