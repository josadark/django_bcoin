import csv
import datetime
import json

from six.moves import urllib
import tushare as ts


nUrl = 'https://eodhistoricaldata.com/api/eod-bulk-last-day/US?api_token=60ec8900a99475.84877251&fmt=json'
response = urllib.request.urlopen(nUrl)
data = json.loads(response.read())

def read_lines(file_path):
    lines = []
    with open(file_path) as f:
        for line in f:
            lines.append(line.strip())
    return lines
def dataUpdate(tickerList,directory):
    g = read_lines(tickerList)
    today = datetime.date.today().strftime("%Y-%m-%d")
    with open(directory + 'daily'+ today+'.csv', 'w') as csvfile:
        twriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in data:
                if i['code'] in g:
                    twriter.writerow([i['code'], i['date'], i['open'], i['high'], i['low'], i['close'], i['volume']])
                    with open(directory+ i['code']+'.csv','a') as newFile:
                        writer = csv.writer(newFile)
                        writer.writerow([i['date'],i['open'],i['high'],i['low'],i['close'],i['volume']])
                else:
                    pass

def crytoUpdate():
    with open('tickerlists/alphaCombined.txt' ,'r') as inFile:
        lines = inFile.readlines()
        for ticker in lines:
            item = ticker.strip()
            print(item)
            try:
                with open('landingpad/Crypto/'+item+'.csv','w') as outFile:
                    writer = csv.writer(outFile,delimiter=',')
                    url = 'https://eodhistoricaldata.com/api/eod/'+item+'.CC?api_token=60ec8900a99475.84877251&fmt=json'
                    response = urllib.request.urlopen(url)
                    data = json.loads(response.read())
                    for ticker in data:
                        writer.writerow([item,ticker['high'],ticker['low'],ticker['open'],ticker['close'],ticker['volume'],ticker['date']])
                        try:
                            with open('landingpad/Crypto/'+ ticker['code']+'.csv','a') as newFile:
                                writer = csv.writer(newFile)
                                writer.writerow([ticker['date'],ticker['open'],ticker['high'],ticker['low'],ticker['close'],ticker['volume']])
                        except:
                            print('Cant find'+ ticker['code']+'.csv in landingpad/Crypto/')
            except:
                pass


def tushareUpdate():
    today = datetime.date.today().strftime("%Y-%m-%d")
    pro = ts.pro_api('f76750e93eacb44bd799deddca43c2f19653b34a1a66f570aa143fcd')
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    data.to_csv("landingpad/China"+today + '.csv')




if __name__ == '__main__':
    dataUpdate('tickerlists/yahootickers.txt','landingpad/Crypto/')
    #crytoUpdate()
    #tushareUpdate()
