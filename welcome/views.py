from django.shortcuts import render
from .models import Post
from .models import Stock
from .models import Candle
from .models import StockDatabase
# plotly imports
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#panda imports for csv reading
import pandas as pd
from datetime import datetime

def home(request):
    Stock.objects.all().delete()
    df = pd.read_csv('outfile.csv')
    df = df.fillna(0)
    counter=0
    #Date,Open,High,Low,Close,Adj Close,Volume,ticker
    for i in df.itertuples():
        quickChange = (abs(i[5]-i[2])/((i[5]+i[2])/2))*100
        if(i[2]>i[5]):
            quickChange=quickChange*-1
        print(i[1])
        date_time = datetime.strptime(i[1], '%m/%d/%Y')
        stockRetrieve = Stock(date=date_time,ticker=i[8],open=round(i[2],2),high=round(i[3],2),low=round(i[4],2),close=round(i[5],2),volume=round(i[7],2), change=round(quickChange,2))
        stockRetrieve.save()
    earners = []
    losers = []
    volatile = []
    steady = []
    for stock in Stock.objects.all():
        if (stock.change > 1):
            earners.append(stock)
        elif (stock.change < -1):
            losers.append(stock)
        if(abs(stock.change)>4):
            volatile.append(stock)
        elif(abs(stock.change)<.5) :
            steady.append(stock)

    context = {
        'stocks':Stock.objects.all(),
        'earners':earners,
        'losers':losers,
        'volatiles':volatile,
        'steady':steady

    }


    return render(request, 'welcome/home.html',context)


def about(request):

    Stock.objects.all().delete()
    df = pd.read_csv('outfile.csv')
    df = df.fillna(0)
    counter=0
    #Date,Open,High,Low,Close,Adj Close,Volume,ticker
    for i in df.itertuples():
        quickChange = (abs(i[5]-i[2])/((i[5]+i[2])/2))*100
        if(i[2]>i[5]):
            quickChange=quickChange*-1
        date_time = datetime.strptime(i[1], '%m/%d/%Y')
        stockRetrieve = Stock(date = date_time, ticker=i[8],open=round(i[2],2),high=round(i[3],2),low=round(i[4],2),close=round(i[5],2),volume=round(i[7],2), change=round(quickChange,4))
        stockRetrieve.save()

    dow = pd.read_csv('DOW.csv')
    dow = dow.fillna(0)
    dow.iloc[::-1]
    dowlist = []
    for i in dow.itertuples():
        quickChange = (abs(i[5]-i[2])/((i[5]+i[2])/2))*100
        if(i[2]>i[5]):
            quickChange=quickChange*-1
        date_time = datetime.strptime(i[1], '%Y-%m-%d')
        stockRetrieve = Stock(date = date_time, ticker='DOW',open=round(i[2],2),high=round(i[3],2),low=round(i[4],2),close=round(i[5],2),volume=round(i[7],2), change=round(quickChange,4))
        dowlist.append(stockRetrieve)


    context = {
        'stocks':Stock.objects.all(),
        'DOW':dowlist

    }
    return render(request, 'welcome/about.html',context)

# Create your views here.


## plotly example

def demo_plot_view(request):
    """
    View demonstrating how to display a graph object
    on a web page with Plotly.
    """

    # Fetching data for plotly
    df = pd.read_csv('ETH-USD.csv')

    # List of graph objects for figure.
    # Each object will contain on series of data.
    graphs = []
    figure = go.Candlestick(
                x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                )
    graphs.append(
        figure
    )
    # Setting layout of the figure.
    layout = {
        'title': 'Etherium (ETH)',
        'xaxis_title': 'Date',
        'yaxis_title': 'USD per Unit',
        'height': 420,
        'width': 560,
    }
    # Getting HTML needed to render the plot.
    plot_div = plot({'data': graphs, 'layout': layout},
                    output_type='div')
    figure = go.Bar(x=df['Date'], y=df['Volume'])
    layout={'xaxis_title':'Date','yaxis_title':'Market Volume'}

    graphs = []
    figure = go.Table(
    header=dict(values=list(df.columns),
                fill_color='bisque',
                align='left'),
    cells=dict(values=[df.Date, df.Open, df.High, df.Low, df.Close, df.AdjClose, df.Volume],
               fill_color='white',
               align='left'))
    graphs.append(figure)
    table_div = plot({'data': graphs,},
                        output_type='div')


    #SECOND DIV
    df = pd.read_csv("BTC-USD.csv")

    # List of graph objects for figure.
    # Each object will contain on series of data.
    graphs = []
    figure = go.Candlestick(
                x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                )
    graphs.append(
        figure
    )
    # Setting layout of the figure.
    layout = {
        'title': 'Bitcoin (BTC)',
        'xaxis_title': 'Date',
        'yaxis_title': 'USD per Unit',
        'height': 420,
        'width': 560,
    }
    # Getting HTML needed to render the plot.
    plot_div2 = plot({'data': graphs, 'layout': layout},
                    output_type='div')

    graphs = []
    figure = go.Table(
    header=dict(values=list(df.columns),
                fill_color='bisque',
                align='left'),
    cells=dict(values=[df.Date, df.Open, df.High, df.Low, df.Close, df.AdjClose, df.Volume],
               fill_color='white',
               align='left'))
    graphs.append(figure)
    table_div2 = plot({'data': graphs,},
                        output_type='div')


    #SECOND DIV DONE

    #THIRD DIV

    df = pd.read_csv("USDT-USD.csv")

    # List of graph objects for figure.
    # Each object will contain on series of data.
    graphs = []
    figure = go.Candlestick(
                x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                )
    graphs.append(
        figure
    )
    # Setting layout of the figure.
    layout = {
        'title': 'Tether (USDT)',
        'xaxis_title': 'Date',
        'yaxis_title': 'USD per Unit',
        'height': 420,
        'width': 560,
    }
    # Getting HTML needed to render the plot.
    plot_div3 = plot({'data': graphs, 'layout': layout},
                    output_type='div')

    graphs = []
    figure = go.Table(
    header=dict(values=list(df.columns),
                fill_color='bisque',
                align='left'),
    cells=dict(values=[df.Date, df.Open, df.High, df.Low, df.Close, df.AdjClose, df.Volume],
               fill_color='white',
               align='left'))
    graphs.append(figure)
    table_div3 = plot({'data': graphs,},
                        output_type='div')



    #THIRD DIV DONE

    #SUBPLOT TEST
    df = pd.read_csv("USDT-USD.csv")
    figure = make_subplots(rows=3, cols=1)

    candlefig = go.Candlestick(
                x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                )
    volumefig = go.Bar(x=df['Date'],y=df['Volume'])
    """tablefig = go.Table(
    header=dict(values=list(df.columns),
                fill_color='bisque',
                align='left'),
    cells=dict(values=[df.Date, df.Open, df.High, df.Low, df.Close, df.AdjClose, df.Volume],
               fill_color='white',
               align='left'))"""

    figure.add_trace(candlefig,row=1, col=1)
    figure.add_trace(volumefig,row=2, col=1)
    #figure.add_trace(tablefig,row=3, col=1)
    figure.update_layout(title_text='TICKER')
    figure.update_xaxes(title_text='Date',row=1,col=1)
    figure.update_xaxes(title_text='Date',row=2,col=1)
    #figure.update_xaxes(title_text='Data Table',row=3,col=1)
    figure.update_yaxes(title_text='USD per Unit',row=1,col=1)
    figure.update_yaxes(title_text='Market Volume',row=2,col=1)
    #figure.update_yaxes(title_text='Data Table',row=3,col=1)

    plotPage = plot({'data': figure,},
                        output_type='div')

    #SUBPLOT TEST DONE

    #big page TEST
    """
    files = [
        "ADA-USD.csv",
        "BNB-USD.csv",
        "BTC-USD.csv",
        #"DOGE-USD.csv",
        #"ETH-USD.csv",
        #"USDT-USD.csv"
        ]
    candleCard = make_subplots(rows=len(files)+1, cols=1,subplot_titles=files)
    c = 0
    for i in files:
        df = pd.read_csv(files[c])
        candlefig = go.Candlestick(
                    x=df['Date'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'],
                    )
        candleCard.update_layout(xaxis_rangeslider_visible=False,height=1700)
        candleCard.add_trace(candlefig,row=c+1,col=1)
        #candleCard.update_yaxes(title_text='Price Per '+files[c],row=c,col=1)
        #candleCard.update_xaxes(title_text=''+files[c],row=c,col=1)
        c=c+1
    plotCard = plot({'data': candleCard,},
                        output_type='div')
                        """
    #big page test done


    #applying the html to the context for rendering
    context ={
    'plot_div': plot_div,
    'plot_div2': plot_div2,
    'table_div':table_div,
    'table_div2':table_div2,
    'plot_div3':plot_div3,
    'table_div3':table_div3,
    'plotPage':plotPage,
    #'plotCard':plotCard
    }



    return render(request, 'welcome/demo-plot.html',
                  context)
