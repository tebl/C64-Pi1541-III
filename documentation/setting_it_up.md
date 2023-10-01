# 1> Setting it up
This part of the documentation takes care of setting up your Pi1541-III, taking care of everything needed to enjoy using it after the hardware has previously been [assembled](https://github.com/tebl/C64-Pi1541-III/blob/main/documentation/assembling_one.md). While most of this information would be relevant to any build of a pi1541, this guide will cover the relevant differences for the Pi1541-III in particular - type of display, use of rotary encoder, that kind of *thing*.

- 1> Setting it up
- [2> Video](#2-video)
- [3> Written instructions](#3-written-instructions)
  - [3.1> Preparing SD-card](#31-preparing-sd-card)
  - [3.2> Copying necessary files](#32-copying-necessary-files)
  - [3.3> Edit configuration](#33-edit-configuration)
  - [3.4> Testing it out](#34-testing-it-out)

## 2> Video
[![YouTube image](https://raw.githubusercontent.com/tebl/C64-Pi1541-III/main/gallery/youtube_clip_setup.jpg)](https://youtu.be/a_sJkwbnSls)

## 3> Written instructions
As a video for this exists, I'll try to keep this brief by mainly attempt to supplement the contents of it - if you hate having to pause a video to read a piece of text, then this is the section you wanted. The following sections have been provided, feel free to skip ahead if you feel confident in your own abilities - and - promise to return when you find out that things did not work as expected (or at all).

- [3.1> Preparing SD-card](#31-preparing-sd-card)
- [3.2> Copying necessary files](#32-copying-necessary-files)
- [3.3> Edit configuration](#33-edit-configuration)
- [3.4> Testing it out](#34-testing-it-out)
  
### 3.1> Preparing SD-card
In order to prepare an SD-card, you will first need to have an SD-card and an SD-card reader. The speed isn't all that much of an issue, a *reasonably* priced slower cards will more than likely work - you'll simply end up waiting longer when adding your entire collection of disk files to it. One thing that is **important**, is that you bought a "*reasonably* priced card", if it seemed like too much of a good deal when ordering it online - then it's practically guaranteed to have been produced with a non-existing capacity. Throw them away and get a refund, any data added beyond a certain limit will simply overwrite previous data and you'll have a cycle of corruption that will in no way function. 

The card that you ended up purchasing from a good local electronics vendor (with or without extra steps due to fake products bought), won't have a file system that a Raspberry Pi can boot from - most cards from 16GB and upwards will have been formatted for you with the *exFAT* file system instead. We need it to have *FAT32*, something that most operating systems by anyone other than Microsoft should handle fine (just make sure that you format the correct drive).

If you were to use any version of Microsoft Windows, then all hope is definitely not lost - we just require some third-party tools to do that. There are a few good ones out there, but there's a LOT of spyware, bloatware and straight up ransomware masquerading as such tools - so use one that you're familiar with and trust. The one I tend to use is [fat32format](http://ridgecrop.co.uk/index.htm?fat32format.htm) - it might look like something from a couple of centuries ago, but so is the one that came with MS Windows so here we are then. Make sure that you format the correct drive.

### 3.2> Copying necessary files
From the pi1541 homepage at [https://cbm-pi1541.firebaseapp.com/](https://cbm-pi1541.firebaseapp.com/), download the latest binaries for setting up a new SD-card - open up the archive and copy the **contents** of the Pi1541 directory directly to the root of your SD-card.

Download the [Raspberry Pi Foundation](https://github.com/raspberrypi/firmware/archive/1.20180919.zip) archive, opening it up you need to open the first and only folder on it. Within the subsequent subfolder, named **boot**, you'll need to copy the following files to the root of your SD-card:
- bootcode.bin
- fixup.dat
- start.elf

The final piece are the ROM-files from an actual Commodore 1541 disk drive, but we don't need to look for a chip extractor just yet - the files are thankfully already included as part of the [VICE](http://vice-emu.sourceforge.net/windows.html) emulator. Download the first listed Zip-file, it doesn't matter if you're not going to be able to run it on your non-Microsoft operating system - as mentioned, we only needed a few files. Opening up the archive, head into the first and only folder - copy the following files to the root of your SD-card.
- DRIVES\dos1541
- DRIVES\dos1571
- DRIVES\dos1581
- C64\chargen

In order to verify that the Pi1541-III has been built correctly, it is recommended that you also download a copy of [Ghosts'n Goblins Arcade](https://www.n0stalgia.org/common/pages/releases.php?op=showrelease&id=329). Open up the archive and copy the d64-file to the 1541-folder on your SD-card.

### 3.3> Edit configuration
The configuration for the Pi1541 software can be changed by editing *options.txt*, a file that should previously have been copied over to your SD-card. We will however need to make some changes to it, the Pi1541-III has been dedisgned to be used with very specific components and we need to set some options in order to make things work. I won't go into a huge amount of details, but suffice it to say you should use the default configuration and make the changes listed below to it.

The first change is to tell it that we've built it up as an option B device, all of the Pi1541-variants designed by me have been built in this way. We therefore need to uncomment this line, as such:
```
// If you are using the split line hardware option (ie Option B) then you need to specify this option
splitIECLines = 1
```
Given that the Pi1541-III was designed for use with a physical display, we won't be needing some of the HDMI functionality and can deactivate those (ideally making the device work less, generating less heat, in theory at least). This is done by changing the value to a zero as such:
```
// This option displays the IEC bus activity on the bottom of the Pi's screen
GraphIEC = 0
```
The buzzer on the device can be enabled, this generates some audiotory feedback to let you know that the device is currently doing something. It's not designed to make any kind of realistic noises, but at least you know that it is doing something instead of just hanging on a dodgy disk image.
```
SoundOnGPIO = 1
SoundOnGPIODuration = 1000 // Length of buzz in micro seconds
SoundOnGPIOFreq = 1200 // Frequency of buzz in Hz
```
The display type needs to be set correctly, anything else will simply result in garbage or nothing at all showing up on the screen. For the Pi1541-III specifically I designed it with the 1.3" OLED modules in mind, these are often sold as ssd1306 compatible displays though they are obviously not - for that reason we need to specify the actual display chip found on them (*sh1106*)
```
// If you are using a LCD screen then specify it here
//LCDName = ssd1306_128x64
//LCDName = ssd1306_128x32
LCDName = sh1106_128x64
```
Some custom boot images have been provided as part of the Pi1541-III project, as well as needed tools in order to create them. These can be found within this repository at [/software/xbm_convert](https://github.com/tebl/C64-Pi1541-III/tree/main/software/xbm_convert), the "raw"-files must be copied to the root of your SD-card. These are optional and I'm mainly including this information as I wasn't able to find it elsewhere, the last line is uncommented and changed to point to one of the new logos.
```
// change startup logo on oled - 1541ii or 1541classic
//LcdLogoName = 1541ii
//LcdLogoName = 1541classic
LcdLogoName = logo_pi1541.raw
```
The final change needed is to set it up to read the rotary encoder that we'll be using, this is replaces the previous way of navigating menus via switches:
```
//ROTARY:
//
//    Please see dmRotary.h for full implementation details.
//
RotaryEncoderEnable = 1
```

With all of that done, make sure to save your changes and safely eject your SD-card.

### 3.4> Testing it out
Plug in the SD-card, then let's pause for a bit to talk about safe power supply choices - in general the extremely cheap options will be cheap **because** they omit all of the features that would normally keep them from burning your house down! As the plug is quite common and just about anything takes 5v these days, consider a proper PSU an investment that you'll be using for all of your other projects as well.

So where do you get proper ones then? Usually an electronics vendor that is local to you, if you are potentially able to punch them in the face - then they won't sell you dangerous stuff. What you'll be looking for should have a standard "barrel" plug on it, but if only to give you something more specific to look for - the one I'm using is a MeanWell GST25B05-P1J (you may need a different model depending on where you live in the world).

With the SD-card plugged in and power applied to it (without connecting it to your C64), then it should start up and allow you to browse the menus using the rotary encoder. If nothing happens or it doesn't seem to work right, please retrace your steps to make sure that the configuration is correct - you can also check out the [troubleshooting](https://github.com/tebl/C64-Pi1541-III/blob/main/documentation/troubleshooting.md) section.

Hooking it up to the C64 you may notice that upon starting up, the display may go blank once the boot logo has been shown - this is the default behaviour when a C64 is connected, but have not been powered on. Turning on the C64 you should be able to browse the menu again, navigate into the 1541 folder and look for that copy of [Ghosts'n Goblins Arcade](https://www.n0stalgia.org/common/pages/releases.php?op=showrelease&id=329) that you copied over earlier, click the rotary encoder to have the Pi1541 start emulating a disk drive with that specific disk inserted.

First ensure that you are able to list the disk contents:
```
LOAD "$",8
LIST
```
If that immediately failed with an error without seeing the Pi1541 activity lights lit up, I would usually suspect a quality issue with the i2c level converter module (in my experience, 2 out of 10 are usually faulty). To rule out the C64, either try connecting a real Commodore 1541 disk drive or alternatively a different C64.

If that looked like it worked, then let's just continue along our merry way and start loading up that game:
```
LOAD "*",8,1
RUN
```
With a fully working Pi1541-III you should be able to load the game all the way via an initially loading menu in between, in particular you should look for corruptions on the image that loads at first (usually pointing to a fake 7406 chip). If it hangs during loading, you may have some other issue -usually solved by using a suitable quality PSU for the Raspberry Pi. Check out [troubleshooting](https://github.com/tebl/C64-Pi1541-III/blob/main/documentation/troubleshooting.md) if you're still stuck at this point.