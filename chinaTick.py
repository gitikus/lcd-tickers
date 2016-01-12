import time ,json
import requests
import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

exchangeRate = requests.get('https://currency-api.appspot.com/api/CNY/USD.json')
rate = float(exchangeRate.json()['rate'])


def okcoin_cny():
    okCNYlast = requests.get('https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny')
    return float(okCNYlast.json()['ticker']['last'])

def huobi():
    huobiBook = requests.get('http://api.huobi.com/staticmarket/detail_btc_json.js')
    return str(huobiBook.json()['p_new'])

    #Take CNY converts to USD
def convert_cny_to_usd(cny):
    current = float(cny)
    USDrate = current*rate
    return str(round(USDrate,2))

def main():
    old_joined = 0.0
    while True:
	try:
            huobiLast = huobi()
	    huobiConverted = convert_cny_to_usd(huobiLast)
            #print 'Huobi:',huobiConverted,'| CNY:',huobiLast
	
            okcny = okcoin_cny()
	    okcny = str(round(okcny, 1))
            okcnyConverted = convert_cny_to_usd(okcny)
	    #print 'OKcn:',okcnyConverted,'| CNY:',okcny
	    new_joined = float(huobiLast)+float(okcny)
	    newData = str('h:' + huobiConverted +'| '+ huobiLast +'\no:' + okcnyConverted +'| '+ okcny)
	except Exception ,e:
	    print '[-] ERROR = '+str(e)
	if new_joined > old_joined:
	    lcd.clear()
	    lcd.set_color(0,1,0)
            lcd.message(newData)
	    old_joined = new_joined
	elif new_joined < old_joined:
	    lcd.clear()
	    lcd.set_color(1,0,0)
	    lcd.message(newData)
	    old_joined = new_joined
	else:
	    lcd.clear()
	    lcd.message(newData)
	time.sleep(5)

if __name__ == '__main__':
    while True:
        main()
