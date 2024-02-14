# TFI2CADT01 - I²C address translator

TFI2CADT01 is an I2C device address changer. This function allows you to connect multiple I2C devices with the same address to one master device on the same bus.

![TFI2CADT01A PCB design](/doc/img/TFI2CADT01A_booth_sides.jpg)

That is a common problem in case multiple I2C sensors with the same address (or a limited number of addresses) need to be connected to one I2C master. The purpose of this module is to change the address with which the I2C master calls to the address of the target I2C (slave) device.
The module is based on [LTC4317](https://www.analog.com/media/en/technical-documentation/data-sheets/4317fa.pdf) I2C address translator IC.
The module is designed and optimized for use on Pixhawk-compatible drones, especially UAVs. The design of the module is compatible with the [dronecode connectors standard](https://github.com/pixhawk/Pixhawk-Standards/blob/master/DS-009%20Pixhawk%20Connector%20Standard.pdf).



## Where to get it?

ThunderFly I2C address translator is commercially available from [ThunderFly s.r.o.](https://www.thunderfly.cz/), write an email to info@thunderfly.cz or shop at [Tindie store](https://www.tindie.com/products/thunderfly/tfi2cadt01-i2c-address-translator/).


## Translation function

The called address of the slave device is translated by a logical operation [XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) with the address bits configured in the TFI2CADT01 module. Each TFI2CADT01 port has a different default address. The address of each port can be changed independently by soldering solder jumpers JP1 and JP2.

## Configuration

The default address translation is listed in the following table.

| Port | Solder jumper | XOR value (in hex) | XOR value in binary form |
|---|---|---|---|
| 1 | Disconnected (default) | 0x08 | 0b0001000 |
| 1 | Soldered     | 0x0f | 0b0001111 |
| 2 | Disconnected (default) | 0x78 | 0b1111000 |
| 2 | Soldered     | 0x7f | 0b1111111 |

### Determining the new address of the I2C device

The new device address which should be called by the master could be calculated by doing XOR with the TFI2CADT01 port address and original device address.  The result is the new device address. You can use an [online calculator](https://xor.pw/) to do that. Another approach is determining the new address heuristically by use of the `i2cdetect` command or similar. 

## Example of usage

The TFI2CADT01 could be used with a wide variety of ThunderFly or Pixhawk I²C sensors, here are a few examples.

### Tachometer (RPM) sensors

The TFI2CADT01 could be easily used for the connection of multiple [TFRPM01 tachometer](https://github.com/ThunderFly-aerospace/TFRPM01) sensors, which is especially useful for multi-rotor airframes.

![TFI2CADT01A using multiple TFRPM01 sensors](/doc/img/TFI2CADT01_multi_TFRPM01.jpg)

### Redundant airspeed sensors

The TFI2CADT01 could also fix troubles with the connection of multiple [TFSLOT01 airspeed sensors](https://github.com/ThunderFly-aerospace/TFSLOT01) to one bus. It could be used even for other I2C-based airspeed sensors. That could increase the redundancy, in situations where a failure of the sensor is more probable than failure of the bus itself.

![TFSLOT  airspeed sensor](https://raw.githubusercontent.com/ThunderFly-aerospace/TFSLOT01/TFSLOT01A/doc/img/TFSLOT_1_small.jpg)


### Temperature and hygrometer sensors

For example the [TFHT01](https://github.com/ThunderFly-aerospace/TFHT01) connected by use of TFI2CADT01 allows measuring of temperature and humidity by multiple airframe locations at once.

![TFHT01](https://raw.githubusercontent.com/ThunderFly-aerospace/TFHT01/TFHT01B/doc/img/TFHT01A2.jpg)

## FAQ

### How I can change the I2C addresses used in the Pixhawk to the ones translated by the TFI2CADT01?

The translated addresses might not be recognized by default in the PX4 (that is usually experienced in the case of the SDP3x sensor driver).
One approach to solve that is to create a configuration file named `config.txt` on the SD card as is documented in the [PX4 documentation](https://docs.px4.io/main/en/concept/system_startup.html#replacing-the-system-startup). In this file, you can specify the start commands for the driver of the translated sensors.

Here's an example of the content of the `/etc/config.txt` on the SD card:

```
sdp3x_airspeed start -X -a <translated_address_a>
sdp3x_airspeed start -X -a <translated_address_b>
```

Replace `<translated_address_a>` and `<translated_address_b>` with the actual translated I2C addresses of your sensors. Addresses could be obtained by calculating XOR with the original address. Or it can be obtained with the `i2cdetect` command. 

