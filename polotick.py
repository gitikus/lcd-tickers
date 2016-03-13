import urllib, urllib2
import json
import time
import sys
import Adafruit_CharLCD as LCD
lcd = LCD.Adafruit_CharLCDPlate()

# USAGE: python2 btc_maid 10

pair = sys.argv[1].upper()
refresh = float(sys.argv[2])
def grabTickData(pair):
    '''Returns ticker data for specified pair'''
    try:
        resp = urllib2.urlopen(urllib2.Request('https://poloniex.com/public?command=returnTicker'))
        resp = json.loads(resp.read())
        return resp[pair]
    except Exception as e:
        print e

def grabLoanData():
    try:
        resp = urllib2.urlopen(urllib2.Request('https://poloniex.com/public?command=returnLoanOrders&currency=BTC'))
        resp = json.loads(resp.read())
        return resp['offers']
    except Exception as e:
        print e


def finexLast():
    try:
        url = "https://api.bitfinex.com/v1/pubticker/btcusd"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        lastPrice = data['last_price'].encode('utf-8')
        return lastPrice
    except Exception as e:
        print e

def main():
    while True:
        try:
            data = grabTickData(pair)
            last = data['last']
            loanData =  grabLoanData()
            lowRate = loanData[0]['rate']
	    lowRate = str(float(lowRate) * 100)
            lcd.clear()
            lcd.message(pair[4:] +': '+last + '\n' + 'Loan: ' + lowRate +'%')
            time.sleep(refresh)
            finex = finexLast()
            lcd.clear()
            lcd.message('Finex: ' + finex)
            time.sleep(refresh)
        except Exception as e:
            lcd.message('ERROR')
            print 'Error:', e

if __name__ == '__main__':
    main()
