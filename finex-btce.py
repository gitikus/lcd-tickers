import sys
import time
import urllib, urllib2
import httplib
import json
import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()
command = sys.argv[1]
def main():
  if command == 'day':
    lcd.set_color(0,0,0)
  elif command == 'night':
    lcd.set_color(0,1,0)
  else:
    print 'args- <night> | <day>'    
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
    lcd.message('BTC:' + btcLast + '\n' + ' LTC:' + ltcLast)
    time.sleep(30)


if __name__ == '__main__':
  main()
