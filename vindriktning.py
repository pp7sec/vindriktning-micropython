import machine, time

class vindriktning:
    def __init__(self, rx):
        self.uart = machine.UART(2, 9600, rx=rx)
        self.uart.init(9600, bits=8, parity=None, stop=1)
        self.pm2point5 = 0
        self.pm1 = 0
        self.pm10 = 0

    def get_value(self):
        if self.pm2point5 == 0 and self.pm1 == 0 and self.pm10 == 0:
            while True:
                value = self.uart.read()
                if value and len(value) >= 16:
                    if int(value[0]) == 22 and int(value[1]) == 17 and int(value[2]) == 11:
                        self.pm2point5 = (int(value[5])*256)+int(value[6])
                        self.pm1 = (int(value[9])*256)+int(value[10])
                        self.pm10 = (int(value[13])*256)+int(value[14])
                        return {'PM1.0': self.pm1,'PM2.5': self.pm2point5,'PM10': self.pm10}
        else:
            value = self.uart.read()
            if value and len(value) >= 16:
                if int(value[0]) == 22 and int(value[1]) == 17 and int(value[2]) == 11:
                    self.pm2point5 = (int(value[5])*256)+int(value[6])
                    self.pm1 = (int(value[9])*256)+int(value[10])
                    self.pm10 = (int(value[13])*256)+int(value[14])
                    return {'PM1.0': self.pm1,'PM2.5': self.pm2point5,'PM10': self.pm10}
            else:
                return {'PM1.0': self.pm1,'PM2.5': self.pm2point5,'PM10': self.pm10}
