# Building the Gen 2 Minibot

Most of our team's gen2 Minibots will be built by refreshing an existing Classic Minibot. However, for those who want to build their own from scratch, links are provided here for all the supplies we have used.


## Hardware

### Cost and Parts List

#### The Basic Kit

The basic Gen 2 Minibot costs about $100 (as of November 2020, excluding taxes and shipping).

- Raspberry Pi 3 Model B+: $48.95 from https://www.buyapi.ca/product/raspberry-pi-3-model-b-plus/
- 8 to 16 GB microSD card: about $5 from Walmart or Best Buy or Amazon
- 2WD Chassis Kit: $18.99 from https://www.amazon.ca/YIKESHU-Smart-Robot-Encoder-Battery/dp/B073VHQT6P
- SB Components Motor Control Shield: $15.95 from https://www.buyapi.ca/product/motor-shield-for-the-raspberry-pi/
- Sensors: about $10
  - one HC-SR04 ultrasonic sensor such as https://www.sunfounder.com/ultrasonic-module-hc-sr04-distance-sensor.html
  - two IR sensors, KY-033, MJ5000, TCRT5000 or similar: https://www.amazon.ca/gp/product/B08215B7TF/
- miscellaneous hardware:
  - M3 hardware, assorted (nuts, bolts, washers)
  - M3 nylon standoffs for the Pi, motor control shield, and IR sensors
  - 20 AWG wire and female Dupont connector crimps

Other things you'll need that you probably already have: 
- USB power bank 
- micro USB cable
- 4 AA batteries
- HDMI cable and monitor
- USB keyboard and mouse
- hair elastics (to strap the USB power bank to the chassis)

#### Upgrades for Advanced Functionality

- Replace the two kit motors with ones that have built-in quadrature encoders: add $22 from https://www.robotshop.com/ca/en/micro-6v-160rpm-1201-dc-geared-motor-encoder.html
  - if needed, buy new metal motor mounts so that the motor can be spaced out from the chassis to account for the protruding encoder circuit board: https://www.banggood.com/4PCS-TT-Motor-Metal-Holder-Mount-For-DIY-Robot-Car-p-1611486.html

- Replace the AA batteries with 18650 li-ion batteries, holder, and charger: add about $25
  - 18650 battery holder with switch: https://www.robotshop.com/ca/en/lipo-battery-holder-switch-18650.html
  - 18650 batteries (2): such as from https://www.amazon.ca/s?k=18650+batteries&ref=nb_sb_noss_2
  - 18650 battery charger: https://www.robotshop.com/ca/en/42v-18650-lithium-battery-charger-us-plug.html
- fancy-dancy ultrasonic sensor mounts:  https://www.amazon.ca/gp/product/B07HQGSYJ5/ (or 3D print something)
- Add a wireless game controller: ???

## Software

### Raspberry Pi OS

Download latest "Raspberry Pi OS (32-bit) with desktop" OS image from https://www.raspberrypi.org/downloads/raspberry-pi-os/

Unzip the image file: 2020-08-20-raspios-buster-armhf.img

Use Raspberry Pi Imager (https://www.raspberrypi.org/downloads/) to write this image to a microSD card (minimum 8 GB). (If needed, erase the previous contents of the SD card first)

Connect the Pi to a wired LAN with internet access.

After verifying that all electrical connections are wired correctly, connect the Pi to a monitor and keyboard and boot up the Pi using this microSD card. We recommend using a wired power supply for initial bootup instead of the USB power bank.

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

### Test

That's it! Time to test out your minibot.
