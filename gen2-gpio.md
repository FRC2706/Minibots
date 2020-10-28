# GPIO allocation for gen2 Minibots

## Assumptions:

SB Components MotorShield from https://www.buyapi.ca/product/motor-shield-for-the-raspberry-pi/

The MotorShield provides fixed allocations for control of 4 motors, 4 LEDs, an HC-SR04 ultrasonic sensor, and 2 IR sensors.

2 rotary quadrature enocoders (left and right drivetrain motors)

We need to allocate two GPIO inputs per encoder, that are not already in use by the MotorShield.

### Gen2 Minibot GPIO Reference

```
                               J8
                              .___.              
                     +3V3---1-|O O|--2--+5V
     Left Encoder A GPIO2---3-|O O|--4--+5V
     Left Encoder B GPIO3---5-|O O|--6--GND
      Sensor 1 Echo GPIO4---7-|O O|--8-----GPIO14 Right Encoder A
                       GND--9-|O.O|-10-----GPIO15 Right Encoder B
    Motor 1 Enable GPIO17--11-|O O|-12-----GPIO18 Sensor 2 Echo
 Motor 1 Control + GPIO27--13-|O O|-14--GND
 Motor 1 Control - GPIO22--15-|O O|-16-----GPIO23 Motor 2 Control +
                     +3V3--17-|O O|-18-----GPIO24 Motor 2 Control -
    Motor 3 Enable GPIO10--19-|O.O|-20--GND
 Motor 3 Control + GPIO9 --21-|O O|-22-----GPIO25 Motor 2 Enable
 Motor 3 Control - GPIO11--23-|O O|-24-----GPIO8 Motor 4 Control +
                      GND--25-|O O|-26-----GPIO7 Motor 4 Control -
                reserved---27-|O O|-28---reserved
Ultrasonic Trigger GPIO5---29-|O.O|-30--GND
   Ultrasonic Echo GPIO6---31-|O O|-32-----GPIO12 Motor 4 Enable
    Back Arrow LED GPIO13--33-|O O|-34--GND
    Left Arrow LED GPIO19--35-|O O|-36-----GPIO16 Right Arrow LED
 Forward Arrow LED GPIO26--37-|O O|-38-----GPIO20
                      GND--39-|O O|-40-----GPIO21
                              '---'

```
Unfortunately this allocation leaves only GPIO20 and GPIO21 remaining, and uses up the serial and SPI pins as well.

### Original Raspberry Pi 40-pin GPIO Header Reference

```
                            J8
                           .___.              
                  +3V3---1-|O O|--2--+5V
          (SDA)  GPIO2---3-|O O|--4--+5V
         (SCL1)  GPIO3---5-|O O|--6--GND
    (GPIO_GLCK)  GPIO4---7-|O O|--8-----GPIO14 (TXD0)
                    GND--9-|O.O|-10-----GPIO15 (RXD0)
    (GPIO_GEN0) GPIO17--11-|O O|-12-----GPIO18 (GPIO_GEN1)
    (GPIO_GEN2) GPIO27--13-|O O|-14--GND
    (GPIO_GEN3) GPIO22--15-|O O|-16-----GPIO23 (GPIO_GEN4)
                  +3V3--17-|O O|-18-----GPIO24 (GPIO_GEN5)
     (SPI_MOSI) GPIO10--19-|O.O|-20--GND
     (SPI_MOSO) GPIO9 --21-|O O|-22-----GPIO25 (GPIO_GEN6)
     (SPI_SCLK) GPIO11--23-|O O|-24-----GPIO8  (SPI_C0_N)
                   GND--25-|O O|-26-----GPIO7  (SPI_C1_N)
       (EEPROM) ID_SD---27-|O O|-28-----ID_SC Reserved for ID EEPROM
                GPIO5---29-|O.O|-30--GND
                GPIO6---31-|O O|-32-----GPIO12
                GPIO13--33-|O O|-34--GND
                GPIO19--35-|O O|-36-----GPIO16
                GPIO26--37-|O O|-38-----GPIO20
                   GND--39-|O O|-40-----GPIO21
                           '---'

```
