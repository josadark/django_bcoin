from django.core.management.base import BaseCommand
from django.db import models
from welcome.models import ChinaStock
import pandas as pd
import csv
import os

class Command(BaseCommand):
    help = 'Updates all active CHN Stock django models with the most recent price, volume, and change data available. [!] soon to be deprecated'

    def handle(self, *args, **kwargs): #handle is called when invoked
        for stock in ChinaStock.objects.all():
            updatedTicker = stock.ticker.split('.')[0]
            print(updatedTicker)
            if os.path.exists('landingpad/China/'+stock.ts_code+'.csv'):
                df = pd.read_csv('landingpad/China/'+stock.ts_code+'.csv')
                df = df.fillna(0)
                df = df.tail(1)
                newStock = stock
                print(stock.ticker)
                for i in df.itertuples(1):
                    print("running")
                    newStock.price = i[7]
                    #newStock.high = i[3]
                    #newStock.low = i[4]
                    #newStock.close = i[5]
                    newStock.change = i[10]
                    newStock.volume = i[11]
                    newStock.open = i[4]
                    newStock.high = i[5]
                    newStock.low = i[6]
                    newStock.close=i[7]
                    stock.delete()
                    newStock.save()
        return
