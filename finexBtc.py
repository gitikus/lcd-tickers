import time
import math
import sys
import urllib
import json

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

def main():
  oldPrice = 0.0
  newPrice = 0.0
  while True:
    url = "https://api.bitfinex.com/v1/pubticker/btcusd"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    newPrice = data['last_price'].encode('utf-8')
#    timestmp = float(data['timestamp'])
    if newPrice > oldPrice:
      lcd.clear()
      lcd.set_color(0,1,0)
      lcd.message('+++' + 'BTC:' + newPrice + '+++')  #+  time.gmtime(timestmp))
      oldPrice = newPrice
    elif newPrice < oldPrice:
      lcd.clear()
      lcd.set_color(1,0,0)
      lcd.message('---' + 'BTC:' + newPrice + '---')
      oldPrice = newPrice
    elif newPrice == oldPrice:
      lcd.clear()
      lcd.message('===' + 'BTC:' + newPrice + '===') # + timestmp)
      oldPrice = newPrice
    time.sleep(7.0)

if __name__ == '__main__':
  main()
