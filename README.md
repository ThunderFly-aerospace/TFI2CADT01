# TFI2CADT01
TFI2CADT01 is I2C address changer module. This allows you to connect multiple I2C devices with the same address to one master device and one bus.

A common problem is that the user wants to connect multiple sensors with the same address (or a limited number of addresses) to one I2C master. The purpose of this module is to change the address with which I2C master calls to the address of the target I2C (slave) device. The translation method is described below. 

Module is based on [LTC4317](https://www.analog.com/media/en/technical-documentation/data-sheets/4317fa.pdf) I2C address traslator.

The module is designed and optimized for use on drones especially UAVs. It is compatible with the [dronecode connectors standard]().


## Translation method
The called address of slave device is translated by a logical operation [XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) with the default address in the module. Each port has a different default address. The address of each port can be changed independently by soldering a solder jumper.


## Configuration

Default address translation is listed in following table: 
| Port | Solder jumper | XOR value (in hex) | XOR value in binary form | 
|---|---|---|---|
| 1 | Disconnected | 0x08 | 0b0001000 |
| 1 | Soldered     | 0x0f | 0b0001111 |
| 2 | Disconnected | 0x78 | 0b1111000 |
| 2 | Soldered     | 0x7f | 0b1111111 |


## Example of usage

