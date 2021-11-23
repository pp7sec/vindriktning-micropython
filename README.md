# vindriktning-micropython

#ESP32
```python
vdt = vindriktning(tx=17, rx=16)
value = vdt.get_value()

pm25 = value['pm2point5']
pm1 = value['pm1']
pm10 = value['pm10']
```

![alt text](https://community-assets.home-assistant.io/original/3X/3/4/3466a02665738d7c7528430ea7918df1dd22446b.jpeg)
