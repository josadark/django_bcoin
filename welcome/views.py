import csv
from django.shortcuts import render
from .models import Post
from .models import Stock
from .models import Candle
from .models import StockDatabase
from .models import Profile
from .models import SimpleStock
from .models import StockHandle
from .models import moment
from .models import IPO
from .models import CryptoStock
from .models import StockAsset
from .models import Portfolio
from .models import ChinaStock
from .models import PublicPortfolio
from .models import PublicStockAsset
from .models import Screen
from .models import ScreenAsset

from .forms import PortfolioForm
from .forms import AssetForm
from .forms import ScreenForm

# plotly imports
import plotly.offline as opy
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
#panda imports for csv reading
import pandas as pd
from datetime import datetime

#import for login
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

#import for Redirect
from django.shortcuts import redirect
#import for grabbing csv from webserver self
from django.http import HttpResponse
from background_task import background

@background(schedule=10)
def notify():
    print("strt!")
#    saveHistorical()
#    print("done.")
    saveDaily()
    print('done')
    return

@background(schedule=10)
def repUpdateSurge():
    print('surge updated')
    return

def updateSurge(): #updates surgeportfolio -- also updates customscreens
    for screen in Screen.objects.all():
        screen.screenasset_set.all().delete()
        for stock in Stock.objects.all():
            if stock.volume > screen.minVolume and stock.volume < screen.maxVolume and stock.price > screen.minValue and stock.price < screen.maxValue:
                screenasset = ScreenAsset(value = stock.price, volume = stock.volume, ticker = stock.ticker, screen = screen)
                screenasset.save()

def updateScreens():
        for screen in Screen.objects.all():
            screen.screenasset_set.all().delete()
            for stock in Stock.objects.all():
                if stock.volume > screen.minVolume and stock.volume < screen.maxVolume and stock.price > screen.minValue and stock.price < screen.maxValue:
                    screenasset = ScreenAsset(value = stock.price, volume = stock.volume, ticker = stock.ticker, screen = screen)
                    screenasset.save()

def saveCryptoDaily():
        CryptoStock.objects.all().delete()
        df = pd.read_csv('newcrypto.csv')
        df = df.fillna(0)
        counter=0
        #Date,Open,High,Low,Close,Adj Close,Volume,ticker
        for i in df.itertuples():
            #print(i[1])
            #date_time = datetime.strptime(i[1], '%m/%d/%Y')
            #stockRetrieve = Stock(date=date_time,ticker=i[8],open=round(i[2],2),high=round(i[3],2),low=round(i[4],2),close=round(i[5],2),volume=round(i[7],2), change=round(quickChange,2))
            stockRetrieve = CryptoStock(open = i[2], high = i[3], low = i[4], close = i[5], adjclose = i[6], volume = i[7], ticker = i[8], change=round(((i[2]-i[5])/i[2]),2))
            stockRetrieve.save()
        return

def saveCHNDaily(): #,ts_code,symbol,name,area,industry,list_date
        ChinaStock.objects.all().delete()
        df = pd.read_csv('newchina.csv')
        df = df.fillna(0)
        counter=0
        #Date,Open,High,Low,Close,Adj Close,Volume,ticker
        for i in df.itertuples():
            #print(i[1])
            #date_time = datetime.strptime(i[1], '%m/%d/%Y')
            #stockRetrieve = Stock(date=date_time,ticker=i[8],open=round(i[2],2),high=round(i[3],2),low=round(i[4],2),close=round(i[5],2),volume=round(i[7],2), change=round(quickChange,2))
            stockRetrieve = ChinaStock(ts_code = i[2], ticker = i[3], name=i[4], area=i[5], industry=i[6], list_date=i[7])
            stockRetrieve.save()
        return

def saveDaily():
        Stock.objects.all().delete()
        df = pd.read_csv('FinViz.csv')
        df = df.fillna(0)
        counter=0
        #Date,Open,High,Low,Close,Adj Close,Volume,ticker
        for i in df.itertuples():
            #print(i[1])
            #date_time = datetime.strptime(i[1], '%m/%d/%Y')
            #stockRetrieve = Stock(date=date_time,ticker=i[8],open=round(i[2],2),high=round(i[3],2),low=round(i[4],2),close=round(i[5],2),volume=round(i[7],2), change=round(quickChange,2))
            stockRetrieve = Stock(index = buffer(i[1]), ticker=i[3],company=i[4],sector=i[5],industry=i[6],country=i[7],marketcap=buffer(i[8]),pricetoearnings=buffer(i[9]),price=buffer(i[10]),change=buffer(i[11]),volume=buffer(i[12]),dividend=buffer(i[13]),returnonassets=buffer(i[14]),returnonequity=buffer(i[15]),returnoninvestment=buffer(i[16]),currentR=buffer(i[17]),quickR=buffer(i[18]),longdebtequity=buffer(i[19]),debtequity=buffer(i[20]),grossm=buffer(i[21]),operm=buffer(i[22]),profit=buffer(i[23]),earnings=buffer(i[24]),fwdpe=buffer(i[33]),peg=buffer(i[34]),pricetosales=buffer(i[35]),pricetobook=buffer(i[36]),partcert=buffer(i[37]),pfcf=buffer(i[38]),EPSthisyear=buffer(i[39]),EPSnextyear=buffer(i[40]),EPSpast5year=buffer(i[41]), EPSnext5year=buffer(i[42]), outstanding=buffer(i[49]), float=buffer(i[50]),insiderOwn=buffer(i[51]),insiderTrans=buffer(i[52]),instOwn=buffer(i[53]),instTrans=buffer(i[54]),floatshort=buffer(i[55]),shortratio=buffer(i[56]),averagevolume=buffer(i[57]),perfweek=buffer(i[62]),perfmonth=buffer(i[63]),perfquart=buffer(i[64]),perfhalf=buffer(i[65]),perfyear=buffer(i[66]),perfytd=buffer(i[67]),volatilityw=buffer(i[68]),volatilitym=buffer(i[69]),recom=buffer(i[70]),relativeVolume=buffer(i[72]),beta=buffer(i[77]),ATR=buffer(i[78]),SMA20=buffer(i[79]),SMA50=buffer(i[80]),SMA200=buffer(i[81]),high52=buffer(i[82]),low52=buffer(i[83]),RSI=buffer(i[84]),fromopen=buffer(i[87]),Gap=buffer(i[88]))
            stockRetrieve.save()
        return

def saveIPO():
        IPO.objects.all().delete()
        df = pd.read_csv('IPO.csv')
        df = df.fillna(0)
        counter=0
        #Date,Open,High,Low,Close,Adj Close,Volume,ticker
        for i in df.itertuples():
            #print(i[1])
            #date_time = datetime.strptime(i[1], '%m/%d/%Y')
            #stockRetrieve = Stock(date=date_time,ticker=i[8],open=round(i[2],2),high=round(i[3],2),low=round(i[4],2),close=round(i[5],2),volume=round(i[7],2), change=round(quickChange,2))
            stockRetrieve = IPO(symbol = i[1], company = i[2], exchange = i[3], date = i[4], range = i[5], price = i[6], currency = i[7], shares = i[8], actions = i[9])
            stockRetrieve.save()
        return



def saveHistorical():
#            print('cronjob is indiana jones!')
            moment.objects.all().delete()
            StockHandle.objects.all().delete()
#            print('cronjob is on a killing spree!')
#            df = pd.read_csv('test.csv')
#            print('cronjob is literate!')
#            df = df.fillna(0)
#            previousStock = 'TWOU'
#            thisStock='TWOU'
#            aStockHandle = StockHandle(ticker='TWOU')
#            aStockHandle.save()
#            for i in df.itertuples():
#                thisStock= i[8]
#                print(thisStock)
#                if thisStock != previousStock:
#                    aStockHandle.save()
#                    aStockHandle = StockHandle(ticker=i[8])
#                    aStockHandle.save()
#                    previousStock=thisStock
#                print('still thy beating heart, says cronjob!')
#                if True:
#                    print('its a cronjob not a conjob')
#                    date_time = datetime.strptime(i[1], '%m/%d/%Y')
#                    stockRetrieve = moment(date=date_time,open=round(float(i[2]),2),high=round(float(i[3]),2),low=round(float(i[4]),2),close=round(float(i[5]),2),adjclose=round(float(i[6]),2),volume=round(float(i[7]),2))
#                    stockRetrieve.save()
#                    aStockHandle.moments.add(stockRetrieve)
#                    print('stored a moment!')
#                print('did i store a moment?')

def logout_view(request):
    logout(request)
    return redirect('welcome-home')
    return render(request, 'welcome/logout.html')

def login_view(request):
    username = password = ''
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("user auth")
        return redirect('welcome-home')
    else:
        ...
        #print("failed login attempt by "+username+" with "+password)

    return render(request, 'welcome/login.html')


def portfolio_view(request):
    isLoggedIn = request.user.is_authenticated
    portfolios=[]
    portfolioNames=[]
    portfolioValues=[]
    portfolioCosts=[]
    portfolioGains=[]
    if(isLoggedIn):
        portfolio = request.user.profile.portfolio.all()
        portfolio = Portfolio.objects.all()

        for port in portfolio:
            port.sunkvalue = 0
            port.value = 0
            for sa in (port.stockasset_set.all()):
                port.sunkvalue = port.sunkvalue + sa.buyPrice * sa.quantity
                port.value = port.value + (sa.value * sa.quantity)
                port.earnings = round(port.value - port.sunkvalue,2)
                port.change = round(100*((port.value - port.sunkvalue) / port.sunkvalue), 2)

        for i in portfolio:
            portfolios.append(i)
            portfolioNames.append(i.title)
            portfolioValues.append(i.value)
            portfolioCosts.append(i.sunkvalue)
            portfolioGains.append(i.earnings)
            print('loaded!')
        colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
        fig = make_subplots(rows=1, cols=3, specs=[[{"type":"pie"}, {"type":"pie"}, {"type":"pie"}]], subplot_titles=("Portfolio Values","Portfolio Costs", "Portfolio Gains"), horizontal_spacing=.25)
        fig.add_trace(go.Pie(labels=portfolioNames, values=portfolioValues), row=1, col=1)
        fig.add_trace(go.Pie(labels=portfolioNames, values=portfolioCosts), row=1, col=2)
        fig.add_trace(go.Pie(labels=portfolioNames, values=portfolioGains), row=1, col=3)
        fig.update_layout(height=500, width=1200, title_text="")
        fig.update_layout(margin = dict(t=0, l=0, r=0, b=0), paper_bgcolor="#fafafa")
        fig.update_traces(hoverinfo='label+percent', textinfo='label', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
        div = opy.plot(fig, auto_open=False, output_type='div')

        publicPortfolios = PublicPortfolio.objects.all()
    context = {'isLoggedIn':isLoggedIn, 'portfolios':portfolios, 'volatiles':Stock.objects.all(), 'publicPortfolios':publicPortfolios, 'graph':div}
    return render(request, 'welcome/portfolio.html', context)

def suggestions(request):
    isLoggedIn = request.user.is_authenticated

    publicPortfolios = PublicPortfolio.objects.all()
    context = {'isLoggedIn':isLoggedIn, 'volatiles':Stock.objects.all(), 'publicPortfolios':publicPortfolios}
    return render(request, 'welcome/suggestions.html', context)

def screens(request):
    isLoggedIn = request.user.is_authenticated
    portfolios=[]
    if(isLoggedIn):
        screens = request.user.screen_set.all()
        portfolio = Portfolio.objects.all()

        for port in portfolio:
            port.sunkvalue = 0
            port.value = 0
            for sa in (port.stockasset_set.all()):
                port.sunkvalue = port.sunkvalue + sa.buyPrice * sa.quantity
                port.value = port.value + (sa.value * sa.quantity)
                port.earnings = round(port.value - port.sunkvalue,2)
                port.change = round(100*((port.value - port.sunkvalue) / port.sunkvalue), 2)

        for i in portfolio:
            portfolios.append(i)
            print('loaded!')

        publicPortfolios = PublicPortfolio.objects.all()
    context = {'isLoggedIn':isLoggedIn, 'portfolios':portfolios, 'volatiles':Stock.objects.all(), 'screens':screens}
    return render(request, 'welcome/screens.html', context)

def delete_portfolio(request):
    isLoggedIn = request.user.is_authenticated
    portfolios=[]
    if(isLoggedIn):
        portfolio = request.user.profile.portfolio.all()
        portfolio = Portfolio.objects.all()

        for port in portfolio:
            port.sunkvalue = 0
            port.value = 0
            for sa in (port.stockasset_set.all()):
                port.sunkvalue = port.sunkvalue + sa.buyPrice * sa.quantity
                port.value = port.value + (sa.value * sa.quantity)
                port.earnings = round(port.value - port.sunkvalue,2)
                port.change = round(100*((port.value - port.sunkvalue) / port.sunkvalue), 2)

        for i in portfolio:
            portfolios.append(i)
            print('loaded!')
    context = {'isLoggedIn':isLoggedIn, 'portfolios':portfolios, 'volatiles':Stock.objects.all()}
    return render(request, 'welcome/delete_portfolio.html', context)

def create_portfolio_view(request):
        form = PortfolioForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = PortfolioForm()
            print("form saved!")
            return redirect('welcome-portfolio')
        else:
            print("invalid form?")
        return render(request, 'welcome/create_portfolio.html', {'form': form, 'volatiles':Stock.objects.all()})

def edit_portfolio_fields(request, portfolioID):
        form = PortfolioForm(request.POST or None)
        if form.is_valid():
            form.stockasset_set = Portfolio.objects.get(title=''+portfolioID).stockasset_set.all()
            tempform = form.save(commit = False)
            tempport = Portfolio.objects.get(title=portfolioID)
            tempport.description = tempform.description
            tempport.title = tempform.title
            tempport.save()
            form = PortfolioForm()
            print("form saved!")
            return redirect('welcome-portfolio')
        else:
            print("invalid form?")
        return render(request, 'welcome/create_portfolio.html', {'form': form, 'volatiles':Stock.objects.all()})

def portfolio_addition(request, stockID):
        isLoggedIn = request.user.is_authenticated
        portfolios=[]
        if(isLoggedIn):
            portfolio = request.user.profile.portfolio.all()
            portfolio = Portfolio.objects.all()

            for port in portfolio:
                port.sunkvalue = 0
                port.value = 0
                for sa in (port.stockasset_set.all()):
                    port.sunkvalue = port.sunkvalue + sa.buyPrice * sa.quantity
                    port.value = port.value + (sa.value * sa.quantity)
                    port.earnings = round(port.value - port.sunkvalue,2)
                    port.change = round(100*((port.value - port.sunkvalue) / port.sunkvalue), 2)
            for i in portfolio:
                portfolios.append(i)
                print('loaded!')
        context = {'isLoggedIn':isLoggedIn, 'portfolios':portfolios, 'volatiles':Stock.objects.all(), 'stockID':stockID}
        return render(request, 'welcome/portfolio_addition.html', context)

def adding(request, stockID, portfolioID):
            port = Portfolio.objects.get(title=portfolioID)
            stock = Stock.objects.get(ticker=stockID)
            form = AssetForm(request.POST or None, initial={"ticker":stockID, "buyPrice":stock.price})
            if form.is_valid():
                #form.save(commit=False)
                form.Portfolio = port
                tempform = form.save(commit = False)
                tempform.portfolio = port
                tempform.value = Stock.objects.get(ticker=tempform.ticker).price
                tempform.save()
                form = AssetForm()
                print("form saved!")
                return redirect('welcome-about')
            else:
                print("invalid form?")
            context = {'portfolio':Portfolio.objects.get(title=portfolioID), 'stocks':Portfolio.objects.get(title=''+portfolioID).stockasset_set.all(), 'form':form, 'portfolioID':portfolioID, 'volatiles':Stock.objects.all()}
            return render(request, 'welcome/edit_portfolio.html', context)

def edit_portfolio(request, portfolioID):
        port = Portfolio.objects.get(title=portfolioID)
        form = AssetForm(request.POST or None)
        if form.is_valid():
            #form.save(commit=False)
            form.Portfolio = port
            tempform = form.save(commit = False)
            tempform.portfolio = port
            tempform.value = Stock.objects.get(ticker=tempform.ticker).price
            tempform.save()
            form = AssetForm()
            print("form saved!")
        else:
            print("invalid form?")
        context = {'portfolio':Portfolio.objects.get(title=portfolioID), 'stocks':Portfolio.objects.get(title=''+portfolioID).stockasset_set.all(), 'form':form, 'portfolioID':portfolioID, 'volatiles':Stock.objects.all()}
        return render(request, 'welcome/edit_portfolio.html', context)

def view_portfolio(request, portfolioID):
    portfolio = Portfolio.objects.get(title=''+portfolioID)
    stocks = portfolio.stockasset_set.all()
    portfolio.sunkvalue = 0
    portfolio.value = 0
    stockNames = []
    stockValues = []
    stockGains = []
    stockCosts = []
    for stock in stocks:
        portfolio.sunkvalue = portfolio.sunkvalue + (stock.buyPrice * stock.quantity)
        portfolio.value = portfolio.value + (stock.value * stock.quantity)
        portfolio.earnings = round(portfolio.value - portfolio.sunkvalue,2)
        portfolio.change = round(((portfolio.value - portfolio.sunkvalue) / portfolio.sunkvalue)*100,2)
        stock.earnings = round((stock.value - stock.buyPrice)*stock.quantity, 2)
        stock.change = round(((stock.value - stock.buyPrice)/stock.buyPrice)*100,2)
        stockNames.append(stock.ticker)
        stockValues.append(stock.value)
        stockGains.append(stock.earnings)
        stockCosts.append(stock.buyPrice)
    for stock in stocks:
        print('stock')

    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
    fig = make_subplots(rows=1, cols=3, specs=[[{"type":"pie"}, {"type":"pie"}, {"type":"pie"}]], subplot_titles=("Values","Costs", "Gains"), horizontal_spacing=.1)
    fig.add_trace(go.Pie(labels=stockNames, values=stockValues), row=1, col=1)
    fig.add_trace(go.Pie(labels=stockNames, values=stockCosts), row=1, col=2)
    fig.add_trace(go.Pie(labels=stockNames, values=stockGains), row=1, col=3)
    fig.update_layout(height=500, width=1200, title_text="")
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0), paper_bgcolor="#fafafa")
    fig.update_traces(hoverinfo='label+percent', textinfo='label', textfont_size=20,
              marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    div = opy.plot(fig, auto_open=False, output_type='div')



    context = {'portfolio':portfolio,
    'portfolioID':portfolioID, 'assets':stocks, 'volatiles':Stock.objects.all(), 'graph':div}
    return render(request, 'welcome/view_portfolio.html', context)


def view_public_portfolio(request, portfolioID):
    portfolio = PublicPortfolio.objects.get(title=''+portfolioID)
    stocks = portfolio.publicstockasset_set.all()
    portfolio.sunkvalue = 0
    portfolio.value = 0
    for stock in stocks:
        print('stock')
    context = {'portfolio':portfolio,
    'portfolioID':portfolioID, 'assets':stocks, 'volatiles':Stock.objects.all()}
    return render(request, 'welcome/view_public_portfolio.html', context)

def view_screened(request, portfolioID):
    portfolio = Screen.objects.get(title=''+portfolioID)
    stocks = portfolio.screenasset_set.all()
    for stock in stocks:
        print('stock')
    context = {'portfolio':portfolio,
    'portfolioID':portfolioID, 'assets':stocks, 'volatiles':Stock.objects.all()}
    return render(request, 'welcome/view_screened.html', context)

def create_screen(request):
        isLoggedIn = request.user.is_authenticated
        if(isLoggedIn):
            form = ScreenForm(request.POST or None)
            if form.is_valid():
                tempform = form.save(commit = False)
                tempform.user = request.user
                tempform.save()
                form = ScreenForm()
                print("form saved!")
                updateScreens()
                return redirect('welcome-screens')
            else:
                print("invalid form?")
                return render(request, 'welcome/create_portfolio.html', {'form': form, 'volatiles':Stock.objects.all()})
            return redirect('welcome-screens')

def remove_portfolio_asset(request, portfolioID):
    portfolio = Portfolio.objects.get(title=''+portfolioID)
    stocks = portfolio.stockasset_set.all()
    portfolio.sunkvalue = 0
    portfolio.value = 0
    for stock in stocks:
        portfolio.sunkvalue = portfolio.sunkvalue + (stock.buyPrice * stock.quantity)
        portfolio.value = portfolio.value + (stock.value * stock.quantity)
        portfolio.earnings = round(portfolio.value - portfolio.sunkvalue,2)
        portfolio.change = round(((portfolio.value - portfolio.sunkvalue) / portfolio.sunkvalue)*100,2)
        stock.earnings = round((stock.value - stock.buyPrice)*stock.quantity, 2)
        stock.change = round(((stock.value - stock.buyPrice)/stock.buyPrice)*100,2)
    context = {'portfolio':portfolio,
    'portfolioID':portfolioID, 'assets':stocks, 'volatiles':Stock.objects.all()}
    return render(request, 'welcome/remove_portfolio_asset.html', context)

def add_to_portfolio(request, stockID): #WIP
    portfolio = Portfolio.objects.get(title=''+portfolioID)
    stocks = portfolio.stockasset_set.all()
    portfolio.sunkvalue = 0
    portfolio.value = 0
    for stock in stocks:
        portfolio.sunkvalue = portfolio.sunkvalue + (stock.buyPrice * stock.quantity)
        portfolio.value = portfolio.value + (stock.value * stock.quantity)
        portfolio.earnings = round(portfolio.value - portfolio.sunkvalue,2)
        portfolio.change = round(((portfolio.value - portfolio.sunkvalue) / portfolio.sunkvalue)*100,2)
        stock.earnings = round((stock.value - stock.buyPrice)*stock.quantity, 2)
        stock.change = round(((stock.value - stock.buyPrice)/stock.buyPrice)*100,2)
    for stock in stocks:
        print('stock')
    context = {'portfolio':portfolio,
    'portfolioID':portfolioID, 'assets':stocks, 'volatiles':Stock.objects.all()}
    return render(request, 'welcome/view_portfolio.html', context)

def delete_selected_portfolio(request, portfolioID):
    portfolio = Portfolio.objects.get(title=''+portfolioID)
    stocks = portfolio.stockasset_set.all()
    portfolio.sunkvalue = 0
    portfolio.value = 0
    for stock in stocks:
        portfolio.sunkvalue = portfolio.sunkvalue + (stock.buyPrice * stock.quantity)
        portfolio.value = portfolio.value + (stock.value * stock.quantity)
        portfolio.earnings = round(portfolio.value - portfolio.sunkvalue,2)
        portfolio.change = round(((portfolio.value - portfolio.sunkvalue) / portfolio.sunkvalue)*100,2)
        stock.earnings = round((stock.value - stock.buyPrice)*stock.quantity, 2)
        stock.change = round(((stock.value - stock.buyPrice)/stock.buyPrice)*100,2)
    for stock in stocks:
        print('stock')
    context = {'portfolio':portfolio,
    'portfolioID':portfolioID, 'assets':stocks, 'volatiles':Stock.objects.all()}
    return render(request, 'welcome/delete_selected_portfolio.html', context)

def deleting(request, portfolioID):
    Portfolio.objects.get(title=''+portfolioID).delete()
    return redirect('welcome-portfolio')

def removing_portfolio_asset(request, portfolioID, stockID, stockCount):
    portfolio = Portfolio.objects.get(title=''+portfolioID)
    portfolio.stockasset_set.filter(quantity=stockCount, ticker=stockID).first().delete()
    return redirect('welcome-portfolio')

def buffer(subject):
    subjects=str(subject)
    if subjects == '-':
        return 0
    if '%' in subjects:
        return float(subjects.split("%")[0])
    elif 'M' in subjects:
        if subjects.split('M')[0] is not '':
            return float(subjects.split('M')[0])*1000000
    elif 'B' in subjects:
        return float(subjects.split('B')[0])*100000000
    elif 'K' in subjects:
        return float(subjects.split('K')[0])*1000
    return float(subjects)

def catchHyphens(subject): #maybe obs
    if subject == '-':
        return ''

def removePerc(x):
    if(x == '-'):
        return 0
    return float(x.strip('%'))

def fixVol(x):

    if(x == '-'):
        return 1
    x=buffer(x)
    return float(x)

def home(request):
    notify()
    #saveDaily()
    #saveCHNDaily()
    #updateSurge()
    print('repup')
    #repUpdateSurge(repeat=120, repeat_until=None)
    counter=0
    df = pd.read_csv('FinViz.csv', converters={'Change_x':removePerc, 'Market Cap_x':fixVol})
    df.dropna(inplace=True)

    rangeBounding = [-1.5,1.5]
    fig = px.treemap(df,
                 path=['Sector', 'Industry', 'Ticker'],
                 values='Market Cap_x',
                 color='Change_x',
                 color_continuous_scale='rdylgn',
                 maxdepth=2,
                 branchvalues='total',
                 range_color=rangeBounding,
                 color_continuous_midpoint=0,
                 width=100,
                 height=450
                )
    fig.update_layout(margin = dict(t=2, l=2, r=2, b=2), paper_bgcolor="#fafafa")
    graphdiv = opy.plot(fig, auto_open=False, output_type='div')

    earners = []
    losers = []
    volatile = []
    steady = []
    tech = []
    financial = []
    IPOlist = []
    relavent = []
    surge=[]
    news = ''''''
    for stock in Stock.objects.all():
        news=news+stock.ticker+' '+str(stock.change)+' | '
        if (stock.change > 1):
            earners.append(stock)
        elif (stock.change < -1):
            losers.append(stock)
        if(abs(stock.change)>4):
            volatile.append(stock)
        elif(abs(stock.change)<.5) :
            steady.append(stock)
        if 'Tech' in stock.sector:
             tech.append(stock)
        if 'Fin' in stock.sector:
            financial.append(stock)

    for stock in IPO.objects.all():
        IPOlist.append(stock)

    for stock in PublicPortfolio.objects.first().publicstockasset_set.all():
        surge.append(stock)

    context = {
        'stocks':Stock.objects.all(),
        'earners':earners,
        'losers':losers,
        'volatiles':volatile,
        'steady':steady,
        'tech':tech,
        'financial':financial,
        'ipos':IPOlist,
        'news':news,
        'graph':graphdiv,
        'surge':surge
    }


    return render(request, 'welcome/home.html',context)


def stockview(request, stockID):
    context = {
        'stockID':stockID,
        'stock':Stock.objects.get(ticker=stockID)
    }
    return render(request, 'welcome/stockview.html', context)

def cryptoview(request, stockID):
    context = {
        'stockID':stockID,
        'stock':CryptoStock.objects.get(ticker=stockID)
    }
    return render(request, 'welcome/cryptoview.html', context)

def grabcsv(request, csvID):
    print('GRABBING FILE!')
    print(csvID)
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )
    writer = csv.writer(response)
    print(csvID)
    df = pd.read_csv('landingpad/Crypto/'+csvID+'.csv')
    df = df.fillna(0)
    counter=0
    #Date,Open,High,Low,Close,Adj Close,Volume,ticker
    writer.writerow(['index','Date','Open','High','Low','Close','Adj Close','Volume'])
    for i in df.itertuples():
        writer.writerow(i)
    return response
    #return render(request, 'welcome/home.html', context)


def about(request):
    notify()
    #saveCryptoDaily()
    #saveIPO()

    #Stock.objects.all().delete()
    #df = pd.read_csv('outfile.csv')
    #df = df.fillna(0)
    #counter=0
    #Date,Open,High,Low,Close,Adj Close,Volume,ticker
    #for i in df.itertuples():
    #    if((i[5]+i[2])/2==0):
    #        quickChange=1
    #    else:
    #        quickChange = (abs(i[5]-i[2])/((i[5]+i[2])/2))*100
    #    if(i[2]>i[5]):
    #        quickChange=quickChange*-1
    #    date_time = datetime.strptime(i[1], '%m/%d/%Y')
    #    stockRetrieve = Stock(date = date_time, ticker=i[8],open=round(i[2],2),high=round(i[3],2),low=round(i[4],2),close=round(i[5],2),volume=round(i[7],2), change=round(quickChange,4))
    #    stockRetrieve.save()

    dow = pd.read_csv('DOW.csv')
    dow = dow.fillna(0)
    dow.iloc[::-1]
    dowlist = []
    for i in dow.itertuples():
        quickChange = (abs(i[5]-i[2])/((i[5]+i[2])/2))*100
        if(i[2]>i[5]):
            quickChange=quickChange*-1
        date_time = datetime.strptime(i[1], '%Y-%m-%d')
        stockRetrieve = SimpleStock(date = date_time, ticker='DOW',open=round(i[2],2),high=round(i[3],2),low=round(i[4],2),close=round(i[5],2),volume=round(i[7],2), change=round(quickChange,4))
        dowlist.append(stockRetrieve)


    context = {
        'stocks':Stock.objects.all(),
        'DOW':dowlist,
        'volatiles':Stock.objects.all()

    }
    return render(request, 'welcome/about.html',context)

def crypto(request):

    dow = pd.read_csv('DOW.csv')
    dow = dow.fillna(0)
    dow.iloc[::-1]
    dowlist = []
    for i in dow.itertuples():
        quickChange = (abs(i[5]-i[2])/((i[5]+i[2])/2))*100
        if(i[2]>i[5]):
            quickChange=quickChange*-1
        date_time = datetime.strptime(i[1], '%Y-%m-%d')
        stockRetrieve = SimpleStock(date = date_time, ticker='DOW',open=round(i[2],2),high=round(i[3],2),low=round(i[4],2),close=round(i[5],2),volume=round(i[7],2), change=round(quickChange,4))
        dowlist.append(stockRetrieve)


    context = {
        'stocks':CryptoStock.objects.all(),
        'DOW':dowlist

    }
    return render(request, 'welcome/crypto.html',context)

def chineseMarket(request):

    dow = pd.read_csv('DOW.csv')
    dow = dow.fillna(0)
    dow.iloc[::-1]
    dowlist = []
    for i in dow.itertuples():
        quickChange = (abs(i[5]-i[2])/((i[5]+i[2])/2))*100
        if(i[2]>i[5]):
            quickChange=quickChange*-1
        date_time = datetime.strptime(i[1], '%Y-%m-%d')
        stockRetrieve = SimpleStock(date = date_time, ticker='DOW',open=round(i[2],2),high=round(i[3],2),low=round(i[4],2),close=round(i[5],2),volume=round(i[7],2), change=round(quickChange,4))
        dowlist.append(stockRetrieve)


    context = {
        'stocks':ChinaStock.objects.all(),
        'DOW':dowlist, 'volatiles':Stock.objects.all()
    }
    return render(request, 'welcome/chineseMarket.html',context)




# Create your views here.


## plotly example


def demo_plot_view(request):
    df = pd.read_csv('FinViz.csv')
    df.dropna(inplace=True)

    fig = px.treemap(df,
                 path=['Sector', 'Industry'],
                 values='No._x',
                 color='No._x'
                )


    div = opy.plot(fig, auto_open=False, output_type='div')

    context = {'graph':div}

    #fig.show()


    return render(request, 'welcome/demo-plot.html',
                  context)

def groups(request):
    volumeSurge = []
    for stock in Stock.objects.all():
        print('looking')
        if stock.volume > stock.averagevolume*1.3:
            volumeSurge.append(stock)
            print('yes!')
        context = {'stocks':volumeSurge}
    return render(request, 'welcome/groups.html', context)


def maps(request):
    df = pd.read_csv('FinViz.csv', converters={'Change_x':removePerc, 'Market Cap_x':fixVol})
    df.dropna(inplace=True)

    rangeBounding = [-1.5,1.5]
    fig = px.treemap(df,
                 path=['Sector', 'Industry', 'Ticker'],
                 hover_name='Ticker',
                 labels='Change_x',
                 values='Market Cap_x',
                 color='Change_x',
                 color_continuous_scale='rdylgn',
                 maxdepth=2,
                 branchvalues='total',
                 range_color=rangeBounding,
                 color_continuous_midpoint=0,
                 width=1600,
                 height=800
                )

    fig.data[0].textinfo = 'label+text+value+percent entry'
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0), paper_bgcolor="#fafafa")
    graphdiv = opy.plot(fig, auto_open=False, output_type='div')
# chinadata start
    df = pd.read_csv('newchina.csv')
    df.dropna(inplace=True)

    rangeBounding = [-1.5,1.5]
    fig = px.treemap(df,
                 path=['area', 'industry', 'name'],
                 hover_name='name',
                 labels='name',
                 values='list_date',
                 color='list_date',
                 color_continuous_scale='rdylgn',
                 maxdepth=2,
                 branchvalues='total',
                 range_color=rangeBounding,
                 color_continuous_midpoint=0,
                 width=1600,
                 height=800
                )

    fig.data[0].textinfo = 'label+text+value+percent entry'
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0), paper_bgcolor="#fafafa")
    graphdiv2 = opy.plot(fig, auto_open=False, output_type='div')

#chinadata end


    context = {
    'graph':graphdiv,
    'graph2':graphdiv2,
    'volatiles':Stock.objects.all()
    }
    return render(request, 'welcome/maps.html', context)
