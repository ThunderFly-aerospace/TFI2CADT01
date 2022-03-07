# TFI2CADT01 - I²C address translator

TFI2CADT01 is I2C device address changer. This function allows you to connect multiple I2C devices with the same address to one master device at the same bus.

![TFI2CADT01A PCB design](/doc/img/TFI2CADT01A_booth_sides.jpg)

That is a common problem in case multiple I2C sensors with the same address (or a limited number of addresses) needs to by connected to one I2C master. The purpose of this module is to change the address with which I2C master calls to the address of the target I2C (slave) device.
Module is based on [LTC4317](https://www.analog.com/media/en/technical-documentation/data-sheets/4317fa.pdf) I2C address traslator IC.
The module is designed and optimized for use on Pixhawk compatible drones especially UAVs. The design of the module is compatible with the [dronecode connectors standard](https://github.com/pixhawk/Pixhawk-Standards/blob/master/DS-009%20Pixhawk%20Connector%20Standard.pdf).

## Translation function

The called address of slave device is translated by a logical operation [XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) with the address bits configured in the TFI2CADT01 module. Each TFI2CADT01 port has a different default address. The address of each port can be changed independently by soldering a solder jumper.

## Configuration

Default address translation is listed in following table.

| Port | Solder jumper | XOR value (in hex) | XOR value in binary form | 
|---|---|---|---|
| 1 | Disconnected | 0x08 | 0b0001000 |
| 1 | Soldered     | 0x0f | 0b0001111 |
| 2 | Disconnected | 0x78 | 0b1111000 |
| 2 | Soldered     | 0x7f | 0b1111111 |

### Determining the new address of the I2C device

The new device address which should be called by master could be calculated easily. Just take the the original device address and do an XOR with the TFI2CADT01 port address.  The result is the new device address. For example, you can use an [online calculator](https://xor.pw/). 

## Example of usage


![TFI2CADT01A using multiple sensors](/doc/img/TFI2CADT01_multi_TFRPM01.jpg)


### TFRPM tachometer sensor


### TFSLOT airspeed sensor


### TFHT hygrometr


