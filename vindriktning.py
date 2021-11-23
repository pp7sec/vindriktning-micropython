import machine

class vindriktning:
    def __init__(self, tx, rx):
        self.uart = machine.UART(2, 9600, tx=tx, rx=rx)
        self.uart.init(9600, bits=8, parity=None, stop=1)

    def get_val(self):
        while True:
            value = self.uart.read()
            if value and len(value) >= 16:
                if int(value[0]) == 22 and int(value[1]) == 17 and int(value[2]) == 11:
                    pm2point5 = (int(value[5])*256)+int(value[6])
                    pm1 = (int(value[9])*256)+int(value[10])
                    pm10 = (int(value[13])*256)+int(value[14])
                    return {'PM1.0': pm1,'PM2.5': pm2point5,'PM10': pm10}
