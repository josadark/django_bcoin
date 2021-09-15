from django.core.management.base import BaseCommand
from django.db import models
from welcome.models import Stock
import pandas as pd
import csv
import os

class Command(BaseCommand):
    help = 'Updates all active US Stock django models with the most recent price, volume, and change data available. [!] soon to be deprecated'

    def handle(self, *args, **kwargs): #handle is called when invoked
        for stock in Stock.objects.all():
            if os.path.exists('landingpad/Yahoo/'+stock.ticker+'.csv'):
                df = pd.read_csv('landingpad/Yahoo/'+stock.ticker+'.csv')
                df = df.fillna(0)
                df = df.tail(1)
                newStock = stock
                print(stock.ticker)
                for i in df.itertuples(1):
                    print("running")
                    newStock.price = i[5]
                    #newStock.high = i[3]
                    #newStock.low = i[4]
                    #newStock.close = i[5]
                    newStock.change = float(i[3])-float(stock.price) / (float(stock.price) + 0.001)
                    newStock.volume = i[7]
                    stock.delete()
                    newStock.save()
        return
