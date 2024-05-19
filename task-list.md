# Introduction
I started this tasklist on the 16th of May to keep track of my progress. I'll try to update it regularly so that the git repo has a record of my evolving conception of the project.

# Aims
1. Demonstrate self organisation in natural systems
2. Use computer algorithms to demonstrate how ecological actions have repercussions that cut across scales
3. Learn the basics of computer vision
4. Learn to build stream tables
5. Create some resources that help others to learn to build stream tables

# Components

## Complete
 - A 600 x 900mm stainless steel tray
 - waterproofing for the tray
 - 9 small coloured house tokens
 - A bilge pump controlled by a relay switch
 - A Bluefruit that can control the relay switch and sense bluetooth proximity
 - A filter to keep stream medium from clogging the drain
 - Chose a power source (the lab supply)
 - Recalculated the volume and mass for the full-sized table.
 - Filter for the downstream end of the table
 - A wooden frame to sit on top of the stainless steel table
 - Test a way of setting up a drain and reservoir
 - Test and set the slope of the table (will use car jacks)

## To Build
 - *(time estimate) Description*
 - (2) Finalise the wooden frame to sit on top of the stainless steel table 
 - (5) Test and choose a medium
 - (2) A hose attachment to bring water from the resevoir at the bottom to the top of the stream
 - (8) Code a microcontroller to receive a bluetooth signal and control the speed of a motor
 - (2.5) Test the speed of the motor necessary to deliver a range of flows with minimal lag
 - (6) Get the RPi up high to get good photos of the table
 - (6) Code Bluetooth transmission from the RPi to the microcontroller
 - (14) Code image recognition in the RPi

Total of 45.5 hours estimated

# Task List

## Past (what was done when)

### 6th of May
 - Drilled drain holes in the bed of the stainless tray (Thanks for the help Dave!)

### 11th of May
 - Disassembled axolotl
 - Organised build box
 - Made plastic washers for the drains using the hole saw attachment for the drill
 - Cut the cross-brace out of the stainless tray using the angle grinder
 - Tidied up all sharp burs with the angle grinder

### 14th of May 
- Flashed an OS to an SD card for the RPi

### 15th of May
- Plugged in RPi for first time
- Plugged in RPi camera
- Tested RPi camera from the command line (Thanks for the tips Ant!)
- Reflashed the RPi OS (because I forgot what password I chose yesterday)

- Used liquid nails to patch holes in the bottom of the stainless tray
- Used liquid nails to attach platic washers to the drains of the stainless tray
- Used silastic to seal all holes in the stainless tray

### 16th of May
- Wrote this plan

Worked for about 2.5 hours in the lab
- Did a flood test of the waterproofing and it was a success
- built a filter for the drain
- Tested LDPE as a medium - it was a failure because it just floats
- Rebooted the RPi.

### 17th of May
- Met with Ben Fox to talk about demo day (see below)
- Thought of a simple design to increase the scale of the project
- Emailed Hannah Feldman to ask if she'd like to show any Peter Cullen trust fellows my CST when she hosts them on Monday
- learnt to connect to the RPi via SSH from my chromebook.
- Met with Safiya and talked about where to present and which bits of equipment I will need on Demo Day 

The conversation with Ben will be a real turning point in this project. He liked the diagram that I have showing the interaction between the components and the allegorical meaning of each component. He encouraged me to conceive of the demo day presentation as no more than three messages or experiences and to be clear to myself what those three should be. Ben gave me many ideas for alternative mediums and some suggestions about where they could be obtained. He played with the LDPE and we agreed that its tacky, artificial feel detracted from the aesthetic and experience of the stream table. We agreed that using a natural medium like sand would enhance the experience for participants. Ben suggested that two different grades of medium will make the geomorphic processes more visible (crushed bark and sand together for example).

Ben and I had a talk about his individual maker project (Cybersoil) and how it created a management loop by allowing land managers to 'feel' their soil in a very granular but intuitive way. We talked about the wider context of environmental management moving towards data-based decisions. I expressed the view that intuition has been an important part of environmental management throughout human history and that I'm not comfortable with the modern push to remove it by quantifying and digitising things. I had already decided that I wanted to affect a sense of mystery or wonder in those that interact with the Cybernetic Stream Table. The net effect of our conversation has been to increase my conviction that the Cybernetic Stream Table stimulate people's sense of the mysterious. I will use some tech to accomplish this but the tech won't be my focus and it will be de-emphasised in any presentation of the table. 

Ben changed my thinking about the design of the table. He pointed out that I could temporarily modify one of the tables at the school and thereby attain a much better user experience at a larger scale. It is a bit daunting to increase the scale of my project, but I believe that it is a very good idea. I've re-drawn my plan for the build to reflect the new ideas.

### 18th of May
- Did some calculations about whether the table will be too heavy
- Went to Jaycar and bought a motor controller and a 12v to 5v transformer
- Studied how the motor controller works (Thanks Muhammed Asfour for your code!)

### 19th of May
- Foud a nice roll of duct tape and a few heavy clamps at home
- Went shopping and bought:
     - Wood lengths
     - Hose fittings

- Built a prototype of the physical component at full scale:                                                                                 - Wood clamped and taped to the table
    - Hooked up hoses
    - Setup a drain and resevoir
    - Hooked up the pump
    - Filled with river sand
    - Tested the types of geomorphic features I can make by tweaking the settings
    - Made a filter to trap most of the sand. 

I feel that the physical component has reached MVP level. There are a couple of different directions I could take to finalise the design of the physical component but I think, at most, it'd take a day's work to polish it off. The microcotroller that I used to build my bluetooth defence Axolotl could already animate the actuation component of the table, so I won't start work on the motor controller yet.  My main concern is that the strength of flow that I have is insuffiecient to rework the sand into a diversity of geomorphic features but I still need to do more testing before making a call on that. As it is, the table is good enough to start collecting photos for the computer vision component, so I will start developing the sensing (computer vision) part of the project now. 

## Future (what I'm aiming to do when)

### 20th of May
- Aim to do 4 hrs
- Maybe show it to some Peter Cullen trust people? They would be the intended user base for the CST.
- Revise the project plan and make sure that the time estimated still matches with the time available.
- Test sticking wood to stainless steel with silastic.
- Figure out what height the photos need to be taken from with the RPi.
- Think about options for mounting the Rpi.

### 21st of May
- Aim to do 8 hrs
- Get some test photos to do computer vision on.
- Write some computer vision code.

### 22nd of May
- Aim to do 9 hrs
- Prototype communication between the components
- Integrated MVP

I'll need to change my focus to other assignments starting on the 23rd. I'd like to reach an integrated MVP by then. The MVP would lack precise control of the motor or sophisticated computer vision. It's physical build will be slightly leaky and fragile but it would essentially have all the components and potentially convey the narrative that I want to get across. That way I'll be finished 2 weeks before demo day and I'll just need to polish it up from then on. 