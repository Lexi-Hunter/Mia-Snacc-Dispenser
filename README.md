# Mia-Snacc-Dispenser
A device that lets you monitor your pet and dispense treats to them
 
<p align="center">
  <img src="https://github.com/Lexi-Hunter/Mia-Snacc-Dispenser/blob/main/Images/MSD_Banner.png">
</p>

## What is the Mia Snacc Dispenser?
The Mia Snacc Dispenser (MSD) is a passion project that I worked on that allows a user to see a live feed of their pet, and then press a button to dispense a treat.
I was motivated to build this device as multiple family members in our house moved away at around the same time, whilst our dog Mia stayed behind. The MSD allows all of my family members to see and interact with Mia regardless of where they are in the world and therefore feel a greater sense of connection.

## How does it work?
A Raspberry Pi Zero W is used to create the site interface along with a Raspberry Pi camera module to capture the live stream. The device is attached to the ceiling so that its contents are out of reach, and so that upon being dispensed, the treat will then drop down and be accessible. A stepper motor is responsible for moving all the treats within the storage area and to dispense exactly one item.

## Site interface
<p align="center">
 <img src="https://github.com/Lexi-Hunter/Mia-Snacc-Dispenser/blob/main/Images/Interface.png" width="700">
</p>

## Real World Implementation
Here is what the device looks like when it is installed on a ceiling:
<p align="center">
 <img src="https://github.com/Lexi-Hunter/Mia-Snacc-Dispenser/blob/main/Images/Real_World_Application.png" width="700">
</p>

## Demo Video
Here is a screen recording of the device being used. Multiple users can access the page simultaneously and dispense treats. In the video my sister and I are both dispensing treats by pressing the button (which is why some treats are dispensed when the button isn't pressed in the recording)

[![MSD Video](https://img.youtube.com/vi/GJGxbpRRaEQ/0.jpg)](https://www.youtube.com/watch?v=GJGxbpRRaEQ)


## How do treats get dispensed?
The device was originally intended to store and dispense sliced carrots as this would be a healthy but tasty option, but upon experimentation, carrots were found to produce too much friction within the mechanism, and the carrot slices would expire faster than anticipated. It was decided that solid dry dog treats would be ideal as they would solve both of these problems.

The V1 of the MSD could store 21 carrot slices by having three platters sitting on top of each other, with 8 rods which can move freely on each platter. This design works by having each rod pushing on a carrot slice around the platter until finally falling onto the platter on the next layer down.

Here is an animation for how this storage and retrieval system works:

![Alt Text](Images/Loading_MSD.gif)

The V2 of the MSD improved upon the first iteration by changing to a substance with a greater shelf life and less friction, whilst also having a smaller volume, allowing for a total of 30 treats stored at once.

Here is the improved design which stores spherical dog treats:
<p align="center">
 <img src="https://github.com/Lexi-Hunter/Mia-Snacc-Dispenser/blob/main/Images/V2_Storage_X_Ray.png" width="700">
</p>

## 3D Printing
In the 3D-Models folder there are the following 4 files that need to be printed and then assembled:
<p align="center">
 <img src="https://github.com/Lexi-Hunter/Mia-Snacc-Dispenser/blob/main/Images/3D_Models.png" width="700">
</p>

## Electronics
Here is an xray view of the underside of the device, where the electronics are stored:

<p align="center">
 <img src="https://github.com/Lexi-Hunter/Mia-Snacc-Dispenser/blob/main/Images/X_Ray_View_Electronics_Diagram.png" width="700">
</p>

## Software
To replicate this project you'll need some basic knowledge of Raspberry Pi, setting up the OS, enabling the camera, etc. Once you have all the basics set up, simply run the Mia_Snacc_Dispenser.py file and it will come to life! It is most useful if you set the python file to auto launch upon booting up, so as soon as the device receives power, it'll auto start the program and just work!

<p align="center">
 <img src="https://github.com/Lexi-Hunter/Mia-Snacc-Dispenser/blob/main/Images/In_Memory_Mia.png" width="700">
</p>
