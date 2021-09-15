import csv
import datetime
import json
import os
import pandas as pd
import time
from datetime import timedelta
from six.moves import urllib
import tushare as ts


def maintask():
    APIKEY = 'b93169c17107c7ada5c4cc1ab50f6fb61777f014'
    tickerList=[]


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
        first=True
        time.sleep(1)
        #with open('landingpad/Crypto/'+ticker1+'-USD'+'.csv','w') as outFile:
        #    writer = csv.writer(outFile,delimiter=',')
            #url = 'https://eodhistoricaldata.com/api/eod/'+item+'.CC?api_token=60ec8900a99475.84877251&fmt=json'
        for i in range(20):
            time.sleep(1)
            url='https://api.nomics.com/v1/currencies/ticker?key='+APIKEY+'&ids='+ticker1+'&interval=1d&convert=USD&per-page=1&page='+str(i)
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())
            print(data)
            if first:
                df = pd.DataFrame(data, columns=["id","currency","name","price","price_date","high","market_cap","max_supply"])
                df.to_csv("landingpad/Crypto/"+ticker1 + '.csv')
                first=False
            else:
                df = pd.DataFrame(data, columns=["id","currency","name","price","price_date","high","market_cap","max_supply"])
                df.to_csv("landingpad/Crypto/"+ticker1 + '.csv', mode='a', header=False)



if __name__ == '__main__':
    #Set start date
    #main program
    maintask()
