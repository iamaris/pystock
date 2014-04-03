import urllib
import pandas as pd
import pandas.io.data as web
import datetime

def getDailyPrice(tckr, startDate, endDate):
    """
    Retrieve historical prices for the given ticker, tckr.
    The date should be formated as 'YYYY-MM-DD'
    
    Returns a nested list.
    """
    s = startDate.split('-')
    e = endDate.split('-')
    url = 'http://ichart.yahoo.com/table.csv?s=%s&' % tckr + \
          'd=%s&' % str(int(e[1]) - 1) + \
          'e=%s&' % str(int(e[2])) + \
          'f=%s&' % str(int(e[0])) + \
          'g=d&' + \
          'a=%s&' % str(int(s[1]) - 1) + \
          'b=%s&' % str(int(s[2])) + \
          'c=%s&' % str(int(s[0])) + \
          'ignore=.csv'
    days = urllib.urlopen(url).readlines()
    quote = [day[:-2].split(',') for day in days]
    
    #return quote[1:]
    return quote


data = getDailyPrice("twtr","2013-11-07","2014-01-22")
#print data
#print data[::-1] 
#Sn+1 = Sn + a(EP- Sn)
#     = (1-a)Sn + a*EP
# initial a = 0.02
# max a = 0.2
# EP = max point in uptrend, min point in downtrend
#a = pd.Series(data)
#print a
#print a.mean()

appl = web.get_data_yahoo('AAPL',start=datetime.datetime(2006, 10, 1),end=datetime.datetime(2012, 1, 1))
print appl
def parabolicSAR():
   print "A"

# Read the stock price data from Yahoo
apple = web.DataReader('AAPL', 'yahoo', start = '01/01/2012', end = '25/10/2012')
 
# Display several lines
apple[0:5]  
 
# Plot closing prices
apple['Close'].plot()
