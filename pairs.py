import urllib
import pandas as pd
import pandas.io.data as web
from datetime import datetime
from datetime import date
import matplotlib.pyplot as plt
	

def getData(_ticker="ZNGA",_startDate="2013-01-01",_endDate="2013-05-01"):
   """
   getData("ZNGA","2012-01-01","2012-01-01")
   where "ZNGA" is the ticker sign of the stock
         "2012-01-01" is the start date //format is YYYY-MM-DD
         "2013-01-01" is the end date   //format is YYYY-MM-DD
   """   
   _s = _startDate.split("-")
   _e = _endDate.split("-")
   return web.DataReader(_ticker, "yahoo", date(int(_s[0]),int(_s[1]),int(_s[2])),date(int(_e[0]),int(_e[1]),int(_e[2])))

def plotPairs(_ticker1,_ticker2):
   _pair = {'ratio':_ticker1['Adj Close']/_ticker2['Adj Close']}
   _pair['ratio'].plot(style='ro')
   plt.ylabel('znga/gluu', fontsize=16)
   plt.axhline(y=_pair['ratio'].mean(),color='r',ls='--')
   plt.axhline(y=_pair['ratio'].mean()-_pair['ratio'].std(),color='b',ls='--')
   plt.axhline(y=_pair['ratio'].mean()+_pair['ratio'].std(),color='b',ls='--')
   plt.plot()
   return 0
"""
d = {'ratio':znga['Adj Close']/gluu['Adj Close'],'znga': znga['Adj Close'], 'gluu': gluu['Adj Close']}

d['ratio'].plot(style='ro')
plt.ylabel('znga/gluu', fontsize=16)
plt.axhline(y=d['ratio'].mean(),color='r',ls='--')
plt.axhline(y=d['ratio'].mean()-d['ratio'].std(),color='b',ls='--')
plt.axhline(y=d['ratio'].mean()+d['ratio'].std(),color='b',ls='--')
plt.show()
"""

"""
sp500 = web.DataReader("^GSPC", "yahoo", datetime(2010,11,15),datetime(2010,12,28))
sbux = web.DataReader("sbux", "yahoo", datetime(2010,11,15),datetime(2010,12,28))
print sbux.head()
#z = znga['Adj Close'].sum()
#g = gluu['Adj Close'].sum()
#zz = znga['Adj Close'].mean()
#gg = gluu['Adj Close'].mean()
both = pd.DataFrame(data = {'asbux/sp500': sbux['Close']/sp500['Adj Close'], 'sbux': sbux['Close'], 'sp500': sp500['Adj Close']})
both_ret = both.pct_change()
print both_ret.head()
print sbux.describe()
print both.cov()
#both.plot()	
#both_ret.plot()	
#plt.show()
"""
