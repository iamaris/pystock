import urllib
import pandas as pd
import pandas.io.data as web
import datetime as dt
import matplotlib.pyplot as plt

#twtr = web.DataReader("twtr", "yahoo", dt.datetime(2013,11,7), dt.datetime.now())
#a = twtr['Adj Close'].plot()
#plt.show()
#print twtr

class stock(object):

   def __init__(self, name="twtr", start=dt.datetime(2013,11,7), end=dt.datetime.now()):
      self.name = name
      self.data = web.DataReader(name, "yahoo", start, end)
      self.open = self.data['Open']
      self.close = self.data['Close']
      self.low   = self.data['Low']
      self.high  = self. data['High']
      self.volume = self.data['Volume']

   def displayData(self):
      print self.data 

   def highest(self):
      return self.close 

   def sma(self,N):
      """simple moving average
      how to use:
      sma(N) where N is the length
      """
      if type(N) != int:
         print "Error: N must be an integer"
  
      avg = self.close
      for i in range(1,N):
         avg = avg + self.close.shift(i-1)
      return avg/(N) 

"""
z = znga['Adj Close'].sum()
g = gluu['Adj Close'].sum()
both = pd.DataFrame(data = {'znga': znga['Adj Close'], 'gluu': gluu['Adj Close']})
both_m = pd.DataFrame(data = {'znga': znga['Adj Close']/zz, 'gluu': gluu['Adj Close']/gg})
both_ret = both.pct_change()
print both_ret.head()
both.plot()
both_m.plot()
both_ret.plot()
plt.show()
"""
