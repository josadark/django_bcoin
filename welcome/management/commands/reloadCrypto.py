from django.core.management.base import BaseCommand
from django.db import models
from welcome.models import CryptoStock
import pandas as pd
import csv
import os
import time
import datetime

class Command(BaseCommand):
    help = 'Updates the entire cryptocurrency models with completely new data [!] crypto model needs migration'

    def handle(self, *args, **kwargs): #handle is called when invoked
            today = datetime.date.today().strftime("%Y-%m-%d")
            CryptoStock.objects.all().delete()
            df = pd.read_csv('landingpad/Crypto'+today+'.csv')
            df = df.fillna(0)
            counter=0
            #Date,Open,High,Low,Close,Adj Close,Volume,ticker
            for i in df.itertuples():
                #print(i[1])
                #date_time = datetime.strptime(i[1], '%m/%d/%Y')
                #stockRetrieve = Stock(date=date_time,ticker=i[8],open=round(i[2],2),high=round(i[3],2),low=round(i[4],2),close=round(i[5],2),volume=round(i[7],2), change=round(quickChange,2))
                stockRetrieve = CryptoStock(ticker = i[2], name = i[4], price = i[5], high = i[7], market_cap = i[8], max_supply = i[9])
                stockRetrieve.save()
            return
