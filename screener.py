import pandas as pd
import datetime

def get_files(directory):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    fixedFiles = []
    for f in onlyfiles:
        fixedFiles.append(directory+f)
    return fixedFiles


#create a dictionary from a list of csv files
def create_dict(list_of_files):
    dict_of_files = {}
    for i in list_of_files:
        try:
            df = pd.read_csv(i)
            df.set_index('Date', inplace=True)
            df.truncate(before=get_month_ago(df.index[-1],24))
            dict_of_files[i.split('/')[-1].split('.')[0]] = df
        except(Exception) as e:
            print("Error reading file: " + i)
            print(e)
    return dict_of_files

#get one month ago from today
def get_month_ago(today,n):
    return (datetime.datetime.strptime(today, "%Y-%m-%d") - pd.DateOffset(months=n)).strftime("%Y-%m-%d")


#returns list of dates for a given stock that correlate with a n(x) surge in volume day by day
def getHighVolDates(df,n):
    highVolDates = []
    lastVol = df.iloc[-1]['Volume']
    for row in df.iterrows():
        if row[1]['Volume'] > lastVol*n:
            highVolDates.append(row[0])
        lastVol = row[1]['Volume']
    return highVolDates

#Given a list of dates, return a the highest percentage increase in a the stock's closing price from the surge date
def getHighestPercentIncrease(df,date):
    initialClose = df.loc[date]['Close']
    d = df.loc[date:]
    dMax = d['Close'].max()
    return ((dMax/initialClose)*100) - 100


def screener(df, pct, vol):
    good = []
    dates = getHighVolDates(df,vol)
    for date in dates:
        npct = getHighestPercentIncrease(df,date)
        if (npct >= pct):
            good.append([date,str(npct.round(2))+'%'])
    return good

def recStocks(dic, pct, volSurge):
    ret = []
    for ticker in dic.keys():
        df = dic[ticker]
        try:
            if len(screener(df,pct,volSurge)) > 0:
                ret.append(ticker)
        except:
            pass
    return ret

def data():
    d = create_dict(get_files('landingpad/Yahoo/'))
    date = datetime.datetime.today()
    oneWeek = (date - pd.DateOffset(days=7)).strftime('%Y-%m-%d')
    for ticker in d.keys():
        d[ticker] = d[ticker].truncate(before=oneWeek)
    return d

d = data()
print(recStocks(d,20,2))
