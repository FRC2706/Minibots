# Team 2706 Minibots

Welcome! This repo is for managing the code and resources for our team's fleet of Raspberry Pi based minibots.

There are two versions of the Minibots:

## The Classic Minibot

The "Classic", or O.G. minibots, were created using a Raspberry Pi, an L298 based motor controller (either the CamJam Edukit #3 drop-in board, or an external L298 board), and an HC-SR04 ultrasonic sensor in a custom-wired circuit board to handle the voltage conversion to Pi-safe levels (a resistor ladder). They use 4xAA batteries to power the motors, a USB power pack to power the Pi (either a Pi model 1B or a Pi model 3B+).

The classic minibots are programmed in Python and have been used in our workshops at the Ottawa Public Library.

## The gen2 Minibot

The gen2 minibots are the result of refreshing classic minibots as they age out. Features of the gen2 minibot:
- hardware upgrade to Raspberry Pi model 3B+ or Pi model 4B
- software upgrade to Raspberry Pi OS "Buster"
- a control "hat" which integrates the motor controller, LED outputs, and HC-SR04 sensor interface for simplified wiring
- drive motors with built-in quadrature encoders for more advanced control capability
- use of 18650 lithium ion batteries instead of AA's

The gen2 minibots will, hopefully, be programmable in Python as well as Java.

The intent of our minibots are to serve as an introductory platform for programming both for team outreach (library workshops) as well as for training of our own software students. The minibots are relatively inexpensive and much more portable than a full size FRC robot. While the coding style differs between minibots and FRC robots, the ability to learn basic programming and robotics concepts (including reading of sensors, encoders, and basic closed loop control) will still be useful.
