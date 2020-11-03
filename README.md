# Team 2706 Minibots

Welcome! This repo is for managing the code and resources for our team's fleet of Raspberry Pi based minibots.

There are two versions of the Minibots:

## The Classic Minibot

The "Classic", or O.G. minibots, were created in 2016 and originally used a Raspberry Pi 1 model B and the CamJam Edukit #3 kit. The classic minibots feature:
- either a Pi 1 model B or a Pi model 3B+
- Raspbian Wheezy or Jessie
- either the CamJam Edukit #3 motor controller hat or an L298N external control board
- an HC-SR04 ultrasonic sensor with a voltage divider to drop the output from 5V to 3.3V
- 4xAA batteries to power the motors
- a USB power pack to power the Pi

The classic minibots are programmed in Python and have been used in our workshops at the Ottawa Public Library. Our workshop curriculum was based on the CamJam Edukit worksheets: https://camjam.me/?page_id=1035

## The gen2 Minibot

The gen2 minibots are the result of refreshing classic minibots as they age out or need repairs. The first refresh was done in October 2020. Features of the gen2 minibot:
- hardware upgrade to Raspberry Pi model 3B+
- software upgrade to Raspberry Pi OS "Buster"
- a new control "hat" which integrates the motor controller, 4 LEDs, and built in ultrasonic and IR sensor interfaces with 3.3v levels for simplified wiring
- new drive motors with built-in quadrature encoders for more advanced control capability
- two IR line detection sensors
- one HC-SR04 ultrasonic sensor in a new rigid mount
- switch from AA batteries to 18650 lithium ion rechargeable batteries in a battery holder with an on/off switch
- consistent GPIO assignments and wiring between all minibots (since we standardized on the controller hat)

## Teaching Goals

The intent of our minibots are to serve as:
- a platform for teaching introductory Python programming workshops (e.g. at the library)
- a training tool for our robotics team students (who designed, assembled, and wired them, created the curriculum slides, the workshop code, and regularly present these workshops)
- a fun demo at team STEM outreach events such as Raspberry Pi Jam and Maker Faire
- an independent learning tool for our robotics team software students when the Covid-19 pandemic prevented us from meeting in person.

The minibots are relatively inexpensive (they cost under $100 each) and obviously much more portable than a full size FRC robot. Students could take these home to work with independently. While the coding style differs between minibots and FRC robots, the ability to learn basic programming and robotics concepts (including reading of sensors, encoders, and basic closed loop control) make these a useful tool for beginner to intermediate level learning.
