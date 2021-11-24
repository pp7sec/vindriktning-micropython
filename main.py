import time
from vindriktning import vindriktning

vdt = vindriktning(tx=17, rx=16)

while True:
    time.sleep(1)
    val = vdt.get_value()
    print('PM1.0 : ', val['PM1.0'])
    print('PM2.5 : ', val['PM2.5'])
    print('PM10  : ', val['PM10'])
    print(' ')
