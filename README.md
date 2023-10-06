# Getting Started
## Overview:
This is a quick port/adaptation of the arduino library for Sparkfun's Microview OLED display to Raspberry Pi Pico plain C.

## C code:
Will be uploaded soon with support for SPI, I2C might follow later (if I actually bother to modify the microview board by soldering the relevant jumper)

## Displaying bitmaps
image_to_c_array.py is a python script that reads images of arbitrary format and size and converts them to the monochrome byte arrays you need in order to actually display an image on the display using the memory layout described here:

https://learn.sparkfun.com/tutorials/microview-hookup-guide/oled-memory-map
