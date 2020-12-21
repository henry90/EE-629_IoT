from requests import get
import board
import busio
from circuitpython_i2c_lcd import I2cLcd
from time import sleep

i2c = busio.I2C(board.SCL, board.SDA)
while i2c.try_lock():
    pass
DEFAULT_I2C_ADDR = 0x27
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

#url = 'http://api.openweathermap.org/data/2.5/weather?id=5128581&appid=42404c2e7097f24b44a146ff6ebd4dfe'
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?id=5128581&cnt=7&appid=42404c2e7097f24b44a146ff6ebd4dfe'

while True:
    data = get(url).json()
    temp_data = data('list', 'weather')
    for entry in temp_data:
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr(str(entry['main']))
        #lcd.move_to(0, 1)
        #lcd.putstr(entry['max'])
        sleep(2)