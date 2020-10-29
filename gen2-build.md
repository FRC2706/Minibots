# Building the Gen 2 Minibot

Most of our team's gen2 Minibots will be built by refreshing an existing Classic Minibot. However, in case anyone wants to build their own from scratch, links are provided here for all the supplies.

## Hardware

Chassis baseplate: make your own, or from a 2WD chassis kit such as https://www.amazon.ca/YIKESHU-Smart-Robot-Encoder-Battery/dp/B073VHQT6P

If the included motor mounts are of the T-shaped acrylic variety, then you might need to also get the metal kind with the bolt threads on the bottom, so that the motor can be spaced out from the chassis to account for the protruding circuit board: https://www.banggood.com/4PCS-TT-Motor-Metal-Holder-Mount-For-DIY-Robot-Car-p-1611486.html

Pi: Raspberry Pi 3 Model B+ or Raspberry Pi 4 Model B/1GB

Motor Control Shield: 1x https://www.buyapi.ca/product/motor-shield-for-the-raspberry-pi/

Motors: from chassis kit or 2x https://www.robotshop.com/ca/en/micro-6v-160rpm-1201-dc-geared-motor-encoder.html

Wheels: from chassis kit or 2x https://www.buyapi.ca/product/thin-white-wheel-for-tt-dc-gearbox-motors-65mm-diameter/

Ultrasonic Sensor: any HC-SR04 will do, but these ones have built in JST connectors: https://www.sunfounder.com/ultrasonic-module-hc-sr04-distance-sensor.html

18650 battery holder with switch: https://www.robotshop.com/ca/en/lipo-battery-holder-switch-18650.html

Other stuff:
- 1.25" rolling caster
- 0.25" nylon spacers
- M3 hardware, assorted (nuts, bolts, washers)
- M3 nylon standoffs
- 2 x 18650 batteries, 18650 battery charger
- USB power bank
- hair elastics

## Software

### Raspberry Pi OS

Download latest "Raspberry Pi OS (32-bit) with desktop" OS image from https://www.raspberrypi.org/downloads/raspberry-pi-os/

Unzip the image file: 2020-08-20-raspios-buster-armhf.img

Use Raspberry Pi Imager (https://www.raspberrypi.org/downloads/) to write this image to a microSD card (minimum 8 GB). (If needed, erase the previous contents of the SD card first)

Boot up the Pi using this microSD card.

Open a terminal window and execute the following commands

... sudo apt-get update/upgrade etc

### Install Merge Robotics Minibots software

install by cloning this repo

