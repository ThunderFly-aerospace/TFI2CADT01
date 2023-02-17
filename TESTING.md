# Testování TFI2CADT01

## Automatické testování (doporučeno)
Postup pro automatické testování sám zkontroluje přeloženou adresu I2C zařizení a vyhodnotí, jestli je to správně nebo ne. Jedná se o jupyter notebook, který je nutné spustit lokálně v počítači, který má prístup k SMBUS sběrnici z kernelu. Instrukce a návod k použití je vepsán přímo v notebooku. Test vyžaduje jedno další I2C zařízení (které obsahuje jedinou I2C adresu)

![image](https://user-images.githubusercontent.com/5196729/219703876-addc8ce5-fa70-4049-870a-2a9e302bb628.png)


## Základní (manuální) testování
Základní testování TFI2CADT01 po výrobě lze provést v kompinaci s TFRPM01 pomocí python [skriptu](https://github.com/ThunderFly-aerospace/TFRPM01/blob/TFRPM01C/sw/pymlab/TFRPM_readout.py) postaveném na knihovně [PyMLAB](https://github.com/MLAB-project/pymlab). 


Skript ze složky `/sw/pymlab/` spustíte příkazem:

```
sudo python3 TFRPM_readout.py 0 0x25
sudo python3 TFRPM_readout.py 0 0x58
```

Po úspěšném spuštění by se měly objevit měřené hodnoty. Nyní, pomocí nějaké sondy nebo uzeměním signálového pinu, simulujte čitací signál. Hodnota `count` by měla růst. Pro přesnější měření lze použit signál generovaný osciloskopem nebo jiným zdrojem pilového signálu. 


Výstup pak může vypadat následovně: 

```bash
TFRPM01 test suite.
{'port': '0', 'device': None, 'serial_number': None}
counter module example 

1608153501.8307571; count: 0, freq: 0.00, integration_time: 0.03
1608153502.3609016; count: 0, freq: 0.00, integration_time: 0.56
1608153502.8917809; count: 0, freq: 0.00, integration_time: 1.09
1608153503.4219267; count: 0, freq: 0.00, integration_time: 1.62
1608153503.9529395; count: 0, freq: 0.00, integration_time: 2.15
1608153504.4839747; count: 0, freq: 0.00, integration_time: 2.68
1608153505.0149646; count: 0, freq: 0.00, integration_time: 3.21
1608153505.5448906; count: 0, freq: 0.00, integration_time: 3.74
1608153506.0749886; count: 0, freq: 0.00, integration_time: 4.27
1608153506.6050436; count: 0, freq: 0.00, integration_time: 4.80
1608153507.136024; count: 0, freq: 0.00, integration_time: 5.34
1608153507.6670556; count: 0, freq: 0.00, integration_time: 5.87
1608153508.197005; count: 0, freq: 0.00, integration_time: 6.40
1608153508.728068; count: 0, freq: 0.00, integration_time: 6.93
1608153509.2590628; count: 2, freq: 0.27, integration_time: 7.46
1608153509.7890441; count: 5, freq: 0.63, integration_time: 7.99
1608153510.3190136; count: 8, freq: 0.94, integration_time: 8.52
1608153510.8490016; count: 11, freq: 1.22, integration_time: 9.05
1608153511.3801253; count: 14, freq: 1.46, integration_time: 9.58
```

V prvním sloupci je čas. Následuje počet detekovaných signálů, určená frekvence a čas po kterou je frekvence počitána. 
