# vindriktning-micropython

#ESP32
```python
vdt = vindriktning(tx=17, rx=16)
value = vdt.get_value()

pm25 = value['pm2point5']
pm1 = value['pm1']
pm 10 = value['pm10']
```
