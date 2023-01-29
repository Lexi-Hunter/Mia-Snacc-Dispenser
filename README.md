# Mia-Snacc-Dispenser
A device that lets you monitor your pet and dispense treats to them
 
<p align="center">
  <img src="https://github.com/Lexi-Hunter/Mia-Snacc-Dispenser/blob/main/Images/MSD_Banner.png">
</p>

## What is the Mia Snacc Dispenser?
The Mia Snacc Dispenser (MSD) is a passion project that I worked on that allows a user to see a live feed of their pet, and then press a button to dispense a treat.
I was motivated to build this device as multiple family members in our house moved away at around the same time, whilst our dog Mia stayed behind. The MSD allows all of my family members to see and interact with Mia regardless of where they are in the world and therefore feel a greater sense of connection.

## How does it work?
A Raspberry Pi Zero W is used to create the site interface along with a Raspberry Pi camera module to capture the live stream. The device is attached to the ceiling so that its contents are out of reach, and so that upon being dispensed, the treat will then drop down and be accessible.

## Site interface
<p align="center">
 <img src="https://github.com/Lexi-Hunter/Mia-Snacc-Dispenser/blob/main/Images/Interface.png" width="700">
</p>

## How do treats get dispensed?
The device was originally intended to store and dispense sliced carrots as this would be a healthy but tasty option, but upon experimentation, carrots were found to produce too much friction within the mechanism, and the carrot slices would expire faster than anticipated. It was decided that solid dry dog treats would be ideal as they would solve both of these problems.

The V1 of the MSD could store 21 carrot slices by having three platters sitting on top of each other, with 8 rods which can move freely on each platter. This design works by having each rod pushing on a carrot slice around the platter until finally falling onto the platter on the next layer down.

Here is an animation for how this storage and retrieval system works:

![Alt Text](Images/Loading_MSD.gif)

The V2 of the MSD improved upon the first iteration by changing to a substance with a greater shelf life and less friction, whilst also having a smaller volume, allowing for a total of 30 treats stored at once.

Here is the improved design which stores spherical dog treats:
<p align="center">
 <img src="https://github.com/Lexi-Hunter/Mia-Snacc-Dispenser/blob/main/Images/.png" width="700">
</p>

## Electronics
Here is an xray view of the underside of the device, where the electronics are stored:

<p align="center">
 <img src="https://github.com/Lexi-Hunter/Mia-Snacc-Dispenser/blob/main/Images/X_Ray_View_Electronics_Diagram.png" width="700">
</p>

## Software
To 
