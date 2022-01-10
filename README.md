# TFI2CADT01
TFI2CADT01 is I2C address changer module. This allows you to connect multiple I2C devices with the same address to one master device and one bus.

A common problem is that the user wants to connect multiple sensors with the same address (or a limited number of addresses) to one I2C master. The purpose of this module is to change the address with which I2C master calls to the address of the target I2C (slave) device. The translation method is described below. 

Module is based on [LTC4317](https://www.analog.com/media/en/technical-documentation/data-sheets/4317fa.pdf) I2C address traslator.

The module is designed and optimized for use on drones especially UAVs. It is compatible with the [dronecode connectors standard]().


## Translation method



## Configuration
This module is configured trought 3 resistors for each channal. This module does not 'exist' on the bus and has no own address. The setting of translation address is set by the ratio of the voltage on the two pins to the supply voltage of the circuit.

By default, the module contains resistors with values xxx, xxx, xxx. This setting corresponds to the change 0b00000000. 



## Example of usage

