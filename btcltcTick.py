import time
import urllib, urllib2
import httplib
import json
import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

def main():
  lcd.set_color(1,1,1)
  while True:
    finexResponse = urllib.urlopen("https://api.bitfinex.com/v1/pubticker/btcusd")
    data1 = json.load(urllib2.urlopen('http://btc-e.com/api/2/ltc_usd/ticker'))
    ltcLast = data1['ticker']
    ltcLast = ltcLast['last']
    ltcLast = round(ltcLast, 3)
    ltcLast = str(ltcLast)
   
    data = json.loads(finexResponse.read())
    btcLast = data['last_price'].encode('utf-8')
   
   
    lcd.clear()
    lcd.message('FINEX BTC:' + btcLast + '\n' + 'BTC-E LTC:' + ltcLast)
    time.sleep(20)


if __name__ == '__main__':
  main()
