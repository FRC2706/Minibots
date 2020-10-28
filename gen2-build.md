Recipe for building Gen 2 Minibot

Hardware

Chassis kit: 2WD base kit from Amazon

Pi: Raspberry Pi 3 Model B+ or Raspberry Pi 4 Model B/1GB

Motor Control Shield: 1x https://www.buyapi.ca/product/motor-shield-for-the-raspberry-pi/

Motors: from chassis kit or 2x https://www.robotshop.com/ca/en/micro-6v-160rpm-1201-dc-geared-motor-encoder.html

Wheels: from chassis kit or 2x https://www.buyapi.ca/product/thin-white-wheel-for-tt-dc-gearbox-motors-65mm-diameter/

Ultrasonic Sensor: any HC-SR04 will do, but these ones have built in JST connectors: https://www.sunfounder.com/ultrasonic-module-hc-sr04-distance-sensor.html

18650 battery holder with switch: https://www.robotshop.com/ca/en/lipo-battery-holder-switch-18650.html



Software

Raspberry Pi OS

Download latest "Raspberry Pi OS (32-bit) with desktop" OS image from https://www.raspberrypi.org/downloads/raspberry-pi-os/

Unzip the image file: 2020-08-20-raspios-buster-armhf.img

Use Raspberry Pi Imager (https://www.raspberrypi.org/downloads/) to write this image to a microSD card (minimum 8 GB). (If needed, erase the previous contents of the SD card first)

Boot up the Pi using this microSD card.

Open a terminal window and execute the following commands

Install Merge Robotics Minibots software

