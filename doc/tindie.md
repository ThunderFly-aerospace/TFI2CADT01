### What is it?
TFI2CADT is a device translating addresses of I2C devices on a bus. As a result, multiple I2C slave devices with the same address can be connected to one master device. One TFI2CADT01 allows connecting 3 identical I2C devices (with one address) to one bus. The I2C slave device will be visible under three addresses. 

The module is designed in accordance with the [pixhawk connector dronecode](https://github.com/pixhawk/Pixhawk-Standards/blob/master/DS-009%20Pixhawk%20Connector%20Standard.pdf) standard. Thanks to this, it can be very easily implemented into the existing avionics of your drone.

### Why did we make it?
It often happens that more identical I2C devices (with the same address) need to be connected to one bus. We even had a request for connecting 4-8 RPM tachometers [TFRPM01](https://www.tindie.com/products/thunderfly/tfrpm01-drone-rpm-tachometer-sensor/) to PX4 autopilot.

### What makes it special?
The device is unique in that the address translation takes place in real-time, during communication via I2C. The user software does not have to deal with any multiplexer channels switching or disconnecting individual parts of the bus. This feature also solves the amount of data flow on the bus. All devices are constantly visible for the I2C master device.

###  How does the translation work?
The address translation takes place internally. A logical operation XOR with a preset value is applied to the address sent by the master. The XOR value is different for each channel. 

By default, an XOR value of 0x08 is applied on the first port and a value of 0x78 on the second port. These values can be easily changed to 0x0f and 0x7f respectively, by short-circuiting the solder jumper.

If these changes are still not sufficient, using configuration resistors you can create any XOR translation of the original address of the device. More information about the address change can be found in the datasheet.

###  How do I connect with the translator? 
Connecting the translator is simple. It is just placed between the I2C master and I2C slave devices. TFI2CADT has JST-GH connectors whose connection corresponds to the dronecode standard. 

Using an adequate cable, the translator can be connected to e.g. Arduino, raspberry, or other devices using I2C. The board is equipped with a pair of input ports that are internally interconnected to enable daisy-chain topology.

### How is the translator supported? 

The translator does not need a software configuration and from the point of view of I2C communication is not visible. Thanks to this, it can be used with any I2C bus, therefore it could be used with any Pixhawk autopilot compatible firmware like [PX4](https://px4.io/) or [Ardupilot](https://ardupilot.org/) additionally the usage is not limited to UAVs only.

### What’s included?

- 1x TFI2CADT01A
- Optionally: 
   - [TFCABxxI2C01](https://github.com/ThunderFly-aerospace/TFCAB01) Silicone I2C cable with JST-GH connectors

### Accessories

#### I2C cabling 
Additional I2C cables for connecting to the autopilot are not included in the package. You must purchase the additional cables separately from our [tindie catalog](https://www.tindie.com/stores/thunderfly/). We offer high-quality cables that are compatible with the [Pixhawk standard](https://raw.githubusercontent.com/pixhawk/Pixhawk-Standards/master/DS-009%20Pixhawk%20Connector%20Standard.pdf) and with a [ThunderFly color](https://docs.px4.io/main/en/assembly/cable_wiring.html#i2c-cables) scheme for easy signal identification. Our cables are specifically designed with improved resistance to electromagnetic interference and a silicone insulator that makes them highly flexible.

  * [TFCABxxI2C01 products](https://www.tindie.com/products/30113/)
