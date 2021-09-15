import csv
import datetime
import json
import os
import pandas as pd
import time
from datetime import timedelta
from six.moves import urllib
import tushare as ts


#nUrl = 'https://eodhistoricaldata.com/api/eod-bulk-last-day/US?api_token=613fcace691174.86212124&fmt=json'
#response = urllib.request.urlopen(nUrl)
#data = json.loads(response.read())

def read_lines(file_path):
    lines = []
    with open(file_path) as f:
        for line in f:
            lines.append(line.strip())
    return lines
def dataUpdate(tickerList,directory):
    nUrl = 'https://eodhistoricaldata.com/api/eod-bulk-last-day/US?api_token=613fcace691174.86212124&fmt=json'
    response = urllib.request.urlopen(nUrl)
    data = json.loads(response.read())
    g = read_lines(tickerList)
    today = datetime.date.today().strftime("%Y-%m-%d")
    with open(directory + 'daily'+ today+'.csv', 'w') as csvfile:
        twriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in data:
                if i['code'] in g:
                    twriter.writerow([i['code'], i['date'], i['open'], i['high'], i['low'], i['close'], i['volume']])
                    if os.path.exists(directory+i['code']+'.csv'):
                        with open(directory+ i['code']+'.csv','a') as newFile:
                            writer = csv.writer(newFile)
                            writer.writerow([i['code'], i['date'], i['open'], i['high'], i['low'], i['close'], i['volume']])
                else:
                    pass

def crytoUpdate(): #b93169c17107c7ada5c4cc1ab50f6fb61777f014
    APIKEY = 'b93169c17107c7ada5c4cc1ab50f6fb61777f014'
    tickerList=[]
    first = True


    # build list
    with open('landingpad/tickerlists/cryptotickers.txt' ,'r') as inFile:
        lines = inFile.readlines()
        for ticker in lines:
            item = ticker.strip()
            item = item.split('.')[0]
            print(item)
            tickerList.append(item)
    # build list DONE


    today = datetime.date.today().strftime("%Y-%m-%d")


    for ticker1 in tickerList:
        time.sleep(1)
        #with open('landingpad/Crypto/'+ticker1+'-USD'+'.csv','w') as outFile:
        #    writer = csv.writer(outFile,delimiter=',')
            #url = 'https://eodhistoricaldata.com/api/eod/'+item+'.CC?api_token=60ec8900a99475.84877251&fmt=json'
        url='https://api.nomics.com/v1/currencies/ticker?key='+APIKEY+'&ids='+ticker1+'&interval=1d,30d&convert=USD&per-page=100&page=1'
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        print(data)
        if first:
            df = pd.DataFrame(data, columns=["id","currency","name","price","price_date","high","market_cap","max_supply"])
            df.to_csv("landingpad/Crypto"+today + '.csv')
            first=False
        else:
            df = pd.DataFrame(data, columns=["id","currency","name","price","price_date","high","market_cap","max_supply"])
            df.to_csv("landingpad/Crypto"+today + '.csv', mode='a', header=False)



#def tushareUpdate():
#    today = datetime.date.today().strftime("%Y-%m-%d")
#    pro = ts.pro_api('f76750e93eacb44bd799deddca43c2f19653b34a1a66f570aa143fcd')
    #data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
#    data = ts.get_hist_data('600848',start='2015-01-05',end='2021-01-09')
#    print(data)
#    data.to_csv("landingpad/China"+today + '.csv')

def tushareUpdate():
    tickerList=[]
    first = True
    today = datetime.date.today().strftime("%Y-%m-%d")
    yesterdayUnstripped = datetime.date.today() - timedelta(days = 1)
    yesterday = yesterdayUnstripped.strftime("%Y-%m-%d")
    with open('landingpad/tickerlists/chinesetickers.txt' ,'r') as inFile:
        lines = inFile.readlines()
        for ticker in lines:
            item = ticker.strip()
            item = item.split('.')[0]
            print(item)
            tickerList.append(item)
    today = datetime.date.today().strftime("%Y-%m-%d")
    pro = ts.pro_api('f76750e93eacb44bd799deddca43c2f19653b34a1a66f570aa143fcd')
    #data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    for ticker in tickerList:
        data = ts.get_hist_data(ticker,start=today,end=today)
        code = [ticker]
        data['Code']=code
        print(data)
        if first:
            data.to_csv("landingpad/China"+today + '.csv')
            first=False
        else:
            data.to_csv("landingpad/China"+today + '.csv', mode='a', header=False)


if __name__ == '__main__':
    #dataUpdate('landingpad/tickerlists/yahootickers.txt','landingpad/Yahoo/')
    crytoUpdate()
    tushareUpdate()
