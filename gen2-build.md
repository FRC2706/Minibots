# Building the Gen 2 Minibot

Most of our team's gen2 Minibots will be built by refreshing an existing Classic Minibot. However, for those who want to build their own from scratch, links are provided here for all the supplies we have used.


## Hardware

### Cost

#### The Basic Kit

The basic Gen 2 Minibot costs $x (as of November 2020, excluding taxes and shipping).

- Raspberry Pi: $48.95
- 2WD Chassis Kit: $18.99
- Motor Control Shield: $15.95
- Sensors: about $10 (one ultrasonic sensor, two IR sensors)

Other things you'll need that you might already have: USB power bank, micro USB cable, 4 AA batteries, HDMI cable, monitor, keyboard, mouse, 20 AWG wire, hair elastic

#### Upgrades for Advanced Functionality

- Replace the kit mtors with ones that have built-in encoders: add $21.30
- Replace the AA batteries with 18650 li-ion batteries and charger: about $25

### Parts List

Chassis baseplate: make your own, or from a 2WD chassis kit such as https://www.amazon.ca/YIKESHU-Smart-Robot-Encoder-Battery/dp/B073VHQT6P

If the included motor mounts are of the T-shaped acrylic variety, then you may want to get the metal kind with the bolt threads on the bottom, so that the motor can be spaced out from the chassis to account for the protruding encoder circuit board: https://www.banggood.com/4PCS-TT-Motor-Metal-Holder-Mount-For-DIY-Robot-Car-p-1611486.html

Pi: Raspberry Pi 3 Model B+ (or Raspberry Pi 4 Model B/1GB, but those require extra HDMI dongles): https://www.buyapi.ca/product/raspberry-pi-3-model-b-plus/

Motor Control Shield: https://www.buyapi.ca/product/motor-shield-for-the-raspberry-pi/

Motors (2): "TT" motors from chassis kit or, if you want ones that have built-in quadrature encoders: https://www.robotshop.com/ca/en/micro-6v-160rpm-1201-dc-geared-motor-encoder.html

Wheels (2): from chassis kit or buy your own, you will also need a 1.25" rolling caster

Ultrasonic Sensor: any HC-SR04 will do, but these ones have built in JST connectors: https://www.sunfounder.com/ultrasonic-module-hc-sr04-distance-sensor.html

IR sensors (2): KY-033, MJ5000, TCRT5000 or similar: https://www.amazon.ca/gp/product/B08215B7TF/

18650 battery holder with switch: https://www.robotshop.com/ca/en/lipo-battery-holder-switch-18650.html

Other stuff:
- 0.25" nylon spacers (for the caster, to make the chassis level)
- M3 hardware, assorted (nuts, bolts, washers)
- M3 nylon standoffs for the Pi and motor shield
- wire and female Dupont connector crimps
- 2 x 18650 batteries
- 18650 battery charger
- USB power bank and micro USB cable
- hair elastics (to strap the USB power bank to the chassis)

## Software

### Raspberry Pi OS

Download latest "Raspberry Pi OS (32-bit) with desktop" OS image from https://www.raspberrypi.org/downloads/raspberry-pi-os/

Unzip the image file: 2020-08-20-raspios-buster-armhf.img

Use Raspberry Pi Imager (https://www.raspberrypi.org/downloads/) to write this image to a microSD card (minimum 8 GB). (If needed, erase the previous contents of the SD card first)

Connect the Pi to a wired LAN with internet access.

Boot up the Pi using this microSD card.

On first boot, follow the first-time setup wizards to:
- set up the location and time zone
- change the pi account password to "team2706"
- download and install software updates
- restart

If not prompted for software updates or if the Pi could not access the network on first-time boot, open a terminal window and execute the following commands:

    sudo apt-get update
    sudo apt-get upgrade

### Install Merge Robotics Minibots software

Open a terminal window and execute the following commands:

    git clone https://github.com/frc2706/Minibots.git

