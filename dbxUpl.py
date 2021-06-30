import dropbox
import os
import pandas as pd
import yfinance as yf
import datetime
import time
import tushare as ts

directory = {'/Crypto','/EarningsCalender','/IPO','/Yahoo','/China'} # TODO auto read in
existingDir = 'landingpad/'
 
 
#Drobox Specific Funcitons
def connect_to_dropbox():
    TOKEN = 'yxGPhvX_qb4AAAAAAAAAARTSYmp-ajbb6P3YiWsWs6oCF9pQiiKOjoA5k8MFx-bm'
    try:
        dbx = dropbox.Dropbox(TOKEN)
        print('Connected to Dropbox successfully')
    except Exception as e:
        print(str(e))
    return dbx
 
 
def updateDirectory(dbx):
        try:
            directory=set()
            # dbx object contains all functions that
            # are required to perform actions with dropbox
            files = dbx.files_list_folder('').entries
            print("Reviewing Directory . .. ...")
            for file in files:
                print(file.name)
                directory.add('/'+file.name)
        except Exception as e:
            print(str(e))
 
        print('directories downloaded :')
        print('=========================')
        for directories in directory:
            print(directories)
        print('=========================')
 
def list_files_in_folder(folder_path):
    try:
        # dbx object contains all functions that
        # are required to perform actions with dropbox
        files = dbx.files_list_folder(folder_path).entries
        print("------------Listing Files in Folder------------ ")
        for file in files:
            print(file.name)
    except Exception as e:
        print(str(e))
 
def download(infilePath,outfilePath):
    dbx.files_download_to_file(outfilePath, infilePath)
 
def load(folder_path):
    try:
        files = dbx.files_list_folder(folder_path).entries
        os.mkdir('landingpad'+folder_path)
        for file in files:
            download(folder_path+'/'+file.name, 'landingpad'+folder_path+'/'+file.name)
    except Exception as e:
        print(str(e))
 
#Yahoo Related Functions
def getTickersFromTxt(file):
    with open(file,'r') as tickerFile:
        Lines = tickerFile.readlines()
 
        count = 0
        # Strips the newline character
        flines = []
        for line in Lines:
            count += 1
            flines.append(line.strip())
    return flines
 
 
def makeMaxCSV(ticker):
    dfList=list()
    data = yf.download(ticker,group_by="Ticker",period="max")
    dfList.append(data)
    df = pd.concat(dfList)
    fileName = ticker + ".csv"
    df.to_csv(existingDir + '/crypto/' + fileName)
 
def makeOneMaxCSV(tickerList):
    dfList = list()
    for ticker in tickerList:
        data = yf.download(ticker,group_by="Ticker",period="max")
        data['ticker'] = ticker 
        dfList.append(data)
        print(ticker)
        time.sleep(1.8)
    df = pd.concat(dfList)
    fileName =  "oneMaxY.csv"
    df.to_csv(existingDir + fileName)


def makeCSV(tickerStrings,period):
    df_list = list()
    today = datetime.date.today().strftime("%Y-%m-%d")
    for ticker in tickerStrings:
        try:
            data = yf.download(ticker, group_by="Ticker", period=period)
            data['ticker'] = ticker  # add this column becasue the dataframe doesn't contain a column with the ticker
            df_list.append(data)
            time.sleep(1.8)
        except:
            pass
    # combine all dataframes into a single dataframe
    df = pd.concat(df_list)
    df.to_csv('landingpad/Yahoo/yahooUpdate' + today + '.csv')
 
def makeCSVCrypto(tickerStrings,period):
    df_list = list()
    today = datetime.date.today().strftime("%Y-%m-%d")
    for ticker in tickerStrings:
        try:
            data = yf.download(ticker, group_by="Ticker", period=period)
            data['ticker'] = ticker  # add this column becasue the dataframe doesn't contain a column with the ticker
            df_list.append(data)
            time.sleep(1.8)#To keep the yahoo api under 2000 request per hour
        except:
            pass
    # combine all dataframes into a single dataframe
    df = pd.concat(df_list)
    df.to_csv('landingpad/Crypto/cryptoUpdate' + today + '.csv')
 
#Daily Related Functions
def yahooUpdate(dbx):
    tickerStrings = getTickersFromTxt("tickerlists/yahootickers.txt")
    today = datetime.date.today().strftime("%Y-%m-%d")
    makeCSV(tickerStrings,'1d')
    #dbx.files_upload(open('landingPad/Yahoo/yahooUpdate.csv','rb').read(),'/Yahoo/'+today+'.csv')
 
def cryptoUpdate(dbx):
    tickerStrings = getTickersFromTxt('tickerlists/cryptotickers.txt')
    today = datetime.date.today().strftime("%Y-%m-%d")
    makeCSVCrypto(tickerStrings,'1d')
    #dbx.files_upload(open('landingpad/Crypto/cryptoUpdate.csv','rb').read(),'/Crypto/'+today+'(1).csv')

def tushareUpdate(dbx):
    today = datetime.date.today().strftime("%Y-%m-%d")
    pro = ts.pro_api('f76750e93eacb44bd799deddca43c2f19653b34a1a66f570aa143fcd')
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    data.to_csv("landingpad/China/stocklist_china" + today + ".csv")
    #dbx.files_upload(open('landingpad/China/stocklist_china.csv','rb').read(),'/Yahoo/'+today+'.csv')

#main code run
dbx = connect_to_dropbox()
#for individual CSV'S

#for daily updates
yahooUpdate(dbx)
cryptoUpdate(dbx)
tushareUpdate(dbx)
