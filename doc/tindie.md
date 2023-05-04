### What is it?
TFI2CADT is a device translating addresses of I2C devices on a bus. As a result, multiple I2C slave devices with the same address can be connected to one master device. One TFI2CADT01 allows connecting 3 identical I2C devices (with one address) to one bus. The I2C master device will be visible under three addresses. 

The module is designed in accordance with the [connector dronecode](https://github.com/pixhawk/Pixhawk-Standards/blob/master/DS-009%20Pixhawk%20Connector%20Standard.pdf) standard. Thanks to this, it can be very easily implemented into the existing avionics of your drone.

### Why did we make it?
It often happens that more identical I2C devices (with the same address) need to be connected to one bus. We even had a request for connecting 4-8 RPM tachometers [TFRPM01](https://www.tindie.com/products/thunderfly/tfrpm01-drone-rpm-tachometer-sensor/) to PX4 autopilot.

### What makes it special?
The device is unique in that the address translation takes place in real-time, during the communication via I2C. The user software does not have to deal with any multiplexer channels switching or disconnecting individual parts of the bus. This feature also solves the amount of data flow on the bus. All devices are constantly visible for the I2C master device.

###  How does the translation work?
The address translation takes place internally. A logical operation XOR with a preset value is applied to the address sent by the master. The XOR value is different for each channel. 

By default, an XOR value of 0x08 is applied on the first port and a value of 0x78 on the second port. These values can be easily changed to 0x0f and 0x7f respectively, by short-circuiting the solder jumper.

If these changes are still not sufficient, using configuration resistors you can create any XOR translation of the original address of the device. More information about the address change can be found in the datasheet.

###  How do I connect with the translator? 
Connecting the translator is simple. It is just necessary to connect it between the I2C master and I2C slave devices. TFI2CADT has JST-GH connectors whose connection corresponds to the dronecode standard. 

The translator can be, using an adequate cable, connected to e.g. Arduino, raspberry, or other devices using I2C.

### How is the translator supported? 
The translator is not software configurable and from the point of view of I2C communication is not visible. Thanks to this, it can be used with any I2C bus and the usage is not limited to UAV only.

The board is equipped with a pair of input ports that are internally interconnected.

### What’s included?

- 1x TFI2CADT01A
- 1x JST-GH 4-pin I2C cable in accordance to [cable style](https://docs.px4.io/master/en/assembly/cable_wiring.html#i2c-cables)
