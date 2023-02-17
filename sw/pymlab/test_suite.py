import smbus2 as smbus
from IPython.display import Markdown, display

bus = None

def detect():
    d = []
    for device in range(128):
          try:
             bus.read_byte(device)
             #print(hex(device))
             d.append(device)
          except: # exception if read_byte fails
             pass
    return d

def run_test(smbus_port = 0):
    global bus
    bus = smbus.SMBus(smbus_port)
    
    detected = []
    print("Pripojte zarizeni do vstupniho konektoru a stisknete enter")
    input()
    tmp = detect()

    print("Adresa koncoveho I2C zarizeni je: {}".format(hex(tmp[0])))
    detected.append(tmp[0])

    print("Zapojte zarizeni do prekladaneho vystupu a stisknete enter")
    input("")
    tmp = detect()
    print("Nova I2C adresa je: {}".format(hex(tmp[0])))
    detected.append(tmp[0])

    print("Zapojte zarizeni do druheho prekladaneho vystupu a stisknete enter")
    input("")

    tmp = detect()
    print("Nova I2C adresa je: {}".format(hex(tmp[0])))
    detected.append(tmp[0])

    obtained_translate = set( (detected[0]^detected[1], detected[0]^detected[2]) )

    default_translation = {0x8, 0x78}
    if (default_translation == obtained_translate):
        print("")
        print("Preklad adres funguje dle ocekavani")
    else:
        print(" ")
        print("NEFUNGUJE: Preklad adres nefunguje dle ocekavani.")
        print("Výchozí XOR je {} a {}".format(hex(list(default_translation)[0]), hex(list(default_translation)[1])))
        print("")
        print("Predpoklad:")
        print("{}^{} = {}".format(hex(detected[0]), hex(list(default_translation)[0]), hex(detected[0]^list(default_translation)[0])))
        print("{}^{} = {}".format(hex(detected[0]), hex(list(default_translation)[1]), hex(detected[0]^list(default_translation)[1])))
        print("")
        print("Detekovano:")
        print("{}^{} = {}".format(hex(detected[0]), hex(detected[0]^detected[1]), hex(detected[1])))
        print("{}^{} = {}".format(hex(detected[0]), hex(detected[0]^detected[2]), hex(detected[2])))
        print("")
        print("Zkontrolujte, ze jste pripojeni i2c zarizeni provedli ve sravnem poradi")