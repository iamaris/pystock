import urllib
import pandas as pd
import pandas.io.data as web
from datetime import datetime
import matplotlib.pyplot as plt
import pickle as pk

znga = web.DataReader("ZNGA", "yahoo", datetime(2009,1,1))
gluu = web.DataReader("GLUU", "yahoo", datetime(2009,1,1))
vix = web.DataReader("^vix", "yahoo", datetime(2009,1,1))
socl = web.DataReader("socl", "yahoo", datetime(2009,1,1))
twtr = web.DataReader("twtr", "yahoo", datetime(2009,1,1))
aapl = web.DataReader("aapl", "yahoo", datetime(2009,1,1))
goog = web.DataReader("goog", "yahoo", datetime(2009,1,1))
ixic = web.DataReader("^ixic", "yahoo", datetime(2009,1,1))
dji = web.DataReader("^dji", "yahoo", datetime(2009,1,1))
gspc = web.DataReader("^gspc", "yahoo", datetime(2009,1,1))
print vix.tail(10)
sbux = web.DataReader("sbux", "yahoo", datetime(2010,11,10),datetime(2010,12,28))
#print znga.head()

pk.dump(znga, open( "znga.p", "wb" ))
pk.dump(gluu, open( "gluu.p", "wb" ))
pk.dump(vix, open( "vix.p", "wb" ))
pk.dump(socl, open( "socl.p", "wb" ))
pk.dump(twtr, open( "twtr.p", "wb" ))
pk.dump(aapl, open( "aapl.p", "wb" ))
pk.dump(goog, open( "goog.p", "wb" ))
pk.dump(ixic, open( "ixic.p", "wb" ))
pk.dump(dji, open( "dji.p", "wb" ))
pk.dump(gspc, open( "gspc.p", "wb" ))


#znga2 = pk.load( open( "znga.p", "rb" ) )

#print znga2

z = znga['Adj Close'].sum()
g = gluu['Adj Close'].sum()
zz = znga['Adj Close'].mean()
gg = gluu['Adj Close'].mean()
d = {'ratio':znga['Adj Close']/socl['Adj Close'],'znga': znga['Adj Close'], 'gluu': gluu['Adj Close']}
#both = pd.DataFrame(data = {'znga': znga['Adj Close'], 'socl': socl['Adj Close']})
both = pd.DataFrame(data = {'znga': znga['Adj Close'], 'znga+1': znga['Adj Close'].shift(1)})
"""
both_m = pd.DataFrame(data = {'znga': znga['Adj Close']/zz, 'gluu': gluu['Adj Close']/gg})
both_ret = both.pct_change()
print both_ret.head()
both.plot()
both_m.plot()
both_ret.plot()
plt.show()
"""
#print d.ix['2014-02-03':'2014-02-13']
#print d.get_loc(datetime(2014,3,1))

#print d

d['ratio'].plot()
plt.ylabel('znga/socl', fontsize=16)
plt.axhline(y=d['ratio'].mean(),color='r',ls='--')
plt.axhline(y=d['ratio'].mean()-d['ratio'].std(),color='b',ls='--')
plt.axhline(y=d['ratio'].mean()+d['ratio'].std(),color='b',ls='--')
#plt.show()
#print both.corr(method='pearson')
#print both.corr(method='kendall')
#print both.corr(method='spearman')



