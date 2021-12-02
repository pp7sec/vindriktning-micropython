# vindriktning-micropython

#ESP32
```python
import time
from vindriktning import vindriktning

vdt = vindriktning(rx=16)

while True:
    time.sleep(1)
    val = vdt.get_value()
    print('PM1.0 : ', val['PM1.0'])
    print('PM2.5 : ', val['PM2.5'])
    print('PM10  : ', val['PM10'])
    print(' ')
```

![alt text](https://community-assets.home-assistant.io/original/3X/3/4/3466a02665738d7c7528430ea7918df1dd22446b.jpeg)
