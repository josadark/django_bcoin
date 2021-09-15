import pandas as pd
import time
import datetime
import json
from datetime import timedelta
from six.moves import urllib



def maintask():
    tickerList=[]
    first = True
    today = datetime.date.today().strftime("%Y-%m-%d")
    yesterdayUnstripped = datetime.date.today() - timedelta(days = 90)
    yesterday = yesterdayUnstripped.strftime("%Y-%m-%d")
    with open('landingpad/tickerlists/yahootickers.txt' ,'r') as inFile:
        lines = inFile.readlines()
        for ticker in lines:
            item = ticker.strip()
            item = item.split('.')[0]
            print(item)
            tickerList.append(item)
    today = datetime.date.today().strftime("%Y-%m-%d")

    #data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    for ticker in tickerList:
        #nUrl = 'https://eodhistoricaldata.com/api/eod-bulk-last-day/US?api_token=60ec8900a99475.84877251&fmt=json'
        nUrl='https://eodhistoricaldata.com/api/eod/'+ticker+'.US?from='+yesterday+'&to='+today+'&period=d&api_token=60ec8900a99475.84877251&fmt=json'
        nUrl='https://eodhistoricaldata.com/api/eod/AAPL.US?from=20210701&to=20210909&period=d&api_token=613fcace691174.86212124&fmt=json'
        response = urllib.request.urlopen(nUrl)
        data = json.loads(response.read())
        code = [ticker]
        print(data)
        df = pd.DataFrame(data, columns=["date","open","high","close","low","adjusted_close","volume"])
        df.to_csv("landingpad/Yahoo/"+ticker + '.csv')


if __name__ == '__main__':
    #Set start date
    #startdate = '20210701' # Arbitrary start date
    #enddate = '20210909' # Adjust to current day
    #main program
    maintask()
