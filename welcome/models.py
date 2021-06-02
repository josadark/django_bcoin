from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Candle(models.Model):
    title = models.CharField(max_length=100)
    dataLocation = models.TextField()



    def __str__(self):
        return self.title

class Stock(models.Model): #contains data for stocks, grabbed by webscraper
    ticker = models.CharField(max_length=9)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    high = models.FloatField()
    low = models.FloatField()
    change = models.FloatField()
    date = models.DateField()


class Quote(models.Model): #daily price up and down (same as plotly tables, all data at a point of time)
    ticker = models.CharField(max_length=9)

class StockDatabase(models.Model):
    CSV = models.FileField()
