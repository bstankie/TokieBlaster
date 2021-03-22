import time
from grove.factory import Factory

# LCD 16x2 Characters
lcd = Factory.getDisplay("JHD1802")
rows, cols = lcd.size()
print("LCD model: {}".format(lcd.name))
print("LCD type : {} x {}".format(cols, rows))

lcd.setCursor(0, 0)
lcd.write("hello world!")
lcd.setCursor(0, cols - 1)
lcd.write('X')
lcd.setCursor(rows - 1, 0)
for i in range(cols):
    lcd.write(chr(ord('A') + i))

time.sleep(3)
lcd.clear()