from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    sunkvalue = models.FloatField(default=0.00)
    value = models.FloatField(default=0.00)
    change = models.FloatField(default=0.00)
    earnings = models.FloatField(default = 0.00)
    #assets = models.ManyToManyField(StockAsset, blank=True)
    def __str__(self):
        return self.title

class PublicPortfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    sunkvalue = models.FloatField(default=0.00)
    value = models.FloatField(default=0.00)
    change = models.FloatField(default=0.00)
    earnings = models.FloatField(default = 0.00)
    #assets = models.ManyToManyField(StockAsset, blank=True)
    def __str__(self):
        return self.title

class Screen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    minValue = models.FloatField(default=0.00)
    maxValue = models.FloatField(default=99999.99)
    minVolume = models.FloatField(default=0.00)
    maxVolume = models.FloatField(default = 99990.99)
    maxChange = models.FloatField(default = 300.0)
    minChange = models.FloatField(default = -300.0)
    minShortRatio = models.FloatField(default = 0)
    maxShortRatio = models.FloatField(default = 100)
    minRelativeVolume = models.FloatField(default = 0)
    maxRelativeVolume = models.FloatField(default = 100)
    #assets = models.ManyToManyField(StockAsset, blank=True)
    def __str__(self):
        return self.title

class StockAsset(models.Model):
    ticker = models.CharField(max_length=9)
    date_purchased = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True)
    buyPrice = models.FloatField(default = 0.00)
    value = models.FloatField(default = 0.00)
    change = models.FloatField(default=0.00)
    earnings = models.FloatField(default=0.00)

class PublicStockAsset(models.Model):
    ticker = models.CharField(max_length=9)
    portfolio = models.ForeignKey(PublicPortfolio, on_delete=models.CASCADE, null=True)
    volume = models.IntegerField(default=0.00)
    value = models.FloatField(default=0.00)

class ScreenAsset(models.Model):
    ticker = models.CharField(max_length=9)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, null=True)
    volume = models.IntegerField(default=0.00)
    value = models.FloatField(default=0.00)

class Candle(models.Model):
    title = models.CharField(max_length=100)
    dataLocation = models.TextField()

    def __str__(self):
        return self.title


class moment(models.Model):
    date = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adjclose = models.FloatField()
    volume = models.IntegerField()

class IPO(models.Model):
    symbol = models.CharField(max_length=8)
    company = models.CharField(max_length=64)
    exchange = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    range = models.CharField(max_length=32)
    price = models.CharField(max_length=8)
    currency = models.CharField(max_length=8)
    shares = models.CharField(max_length=8)
    actions = models.CharField(max_length=16)

class StockHandle(models.Model):
    ticker = models.CharField(max_length=9)
    moments = models.ManyToManyField(moment, blank=True)

class Stock(models.Model): #contains data for stocks, grabbed by webscraper
    index = models.IntegerField()
    ticker = models.CharField(max_length=9)
    company = models.CharField(max_length=35)
    sector = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    marketcap = models.FloatField()
    pricetoearnings = models.FloatField()
    price = models.FloatField()
    change = models.FloatField()
    volume = models.FloatField()
    dividend = models.FloatField()
    returnonassets = models.FloatField()
    returnonequity = models.FloatField()
    returnoninvestment = models.FloatField()
    currentR = models.FloatField()
    quickR = models.FloatField()
    longdebtequity = models.FloatField()
    debtequity = models.FloatField()
    grossm = models.FloatField()
    operm = models.FloatField()
    profit = models.FloatField()
    earnings = models.FloatField()
    fwdpe = models.FloatField()
    peg = models.FloatField()
    pricetosales = models.FloatField()
    pricetobook = models.FloatField()
    partcert = models.CharField(max_length=8)
    pfcf = models.FloatField()
    EPSthisyear = models.FloatField()
    EPSnextyear = models.FloatField()
    EPSpast5year = models.FloatField()
    EPSnext5year = models.FloatField()
    outstanding = models.FloatField()
    float = models.FloatField()
    insiderOwn = models.FloatField()
    insiderTrans = models.FloatField()
    instOwn = models.FloatField()
    instTrans = models.FloatField()
    floatshort = models.FloatField()
    shortratio = models.FloatField()
    averagevolume = models.FloatField()
    perfweek = models.FloatField()
    perfmonth = models.FloatField()
    perfquart = models.FloatField()
    perfhalf = models.FloatField()
    perfyear = models.FloatField()
    perfytd = models.FloatField()
    volatilityw = models.FloatField()
    volatilitym = models.FloatField()
    recom = models.FloatField()
    relativeVolume =models.FloatField()
    beta = models.FloatField()
    ATR = models.FloatField()
    SMA20 = models.FloatField()
    SMA50 = models.FloatField()
    SMA200 = models.FloatField()
    high52 = models.FloatField()
    low52 = models.FloatField()
    RSI = models.FloatField()
    fromopen = models.FloatField()
    Gap = models.FloatField()

class CryptoStock(models.Model): #contains data for stocks, grabbed by webscraper
    ticker = models.CharField(max_length=9)
    open = models.FloatField()
    close = models.FloatField()
    adjclose = models.FloatField()
    volume = models.IntegerField()
    high = models.FloatField()
    low = models.FloatField()
    change = models.FloatField()

class ChinaStock(models.Model):
    #,ts_code,symbol,name,area,industry,list_date
    ts_code = models.CharField(max_length=30)
    ticker = models.CharField(max_length=9)
    name = models.CharField(max_length=9)
    area = models.CharField(max_length=9)
    industry = models.CharField(max_length=9)
    list_date = models.CharField(max_length=9)



    ## obsolete stockdata

    #open = models.FloatField()
    #close = models.FloatField()
    #volume = models.IntegerField()
    #high = models.FloatField()
    #low = models.FloatField()
    #change = models.FloatField()
    #date = models.DateField()

class SimpleStock(models.Model): #historical stock model for use with older charts
    ticker = models.CharField(max_length=9)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    high = models.FloatField()
    low = models.FloatField()
    change = models.FloatField()
    date = models.DateField()

class Quote(models.Model): #daily price up and down (same as plotly tables, all data at a point of time) only used for referencing
    ticker = models.CharField(max_length=9)

class StockDatabase(models.Model):
    CSV = models.FileField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio = models.ManyToManyField(Portfolio, blank=True)

@receiver(post_save, sender=User) #signals to detect updates and profile creations
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
