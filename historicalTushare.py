import tushare as ts
import pandas as pd
import time


def maintask():
    pro = ts.pro_api('f76750e93eacb44bd799deddca43c2f19653b34a1a66f570aa143fcd')
    #Get basic information data, including stock code, name, date of listing, date of delisting, etc.
    pool = pro.stock_basic(exchange = '',
                           list_status = 'L',
                           adj = 'qfq',
                           fields = 'ts_code,symbol,name,area,industry,fullname,list_date, market,exchange,is_hs')
    #print(pool.head())
    print('Get the total number of listed stocks:', len(pool)-1)
    j = 1
    for i in pool.ts_code:
        print('Getting the first %d home, stock code %s.' % (j, i))
        #interface limit access 200 times / minute, add a little delay to prevent being ban
        time.sleep(0.301)
        j += 1
        df = pro.daily(ts_code = i,
                       start_date = startdate,
                       end_date = enddate,
                       fields = 'ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount')
        #print(df.head())
        df.to_csv('landingpad/China/'+i+'.csv')


if __name__ == '__main__':
    #Set start date
    startdate = '19980101'
    enddate = '20200630'
    #main program
    maintask()