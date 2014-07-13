import urllib
import pandas as pd
import pandas.io.data as web
from datetime import datetime
import matplotlib.pyplot as plt
import pickle as pk

king = web.DataReader("king", "yahoo", datetime(2014,1,1))
znga = web.DataReader("ZNGA", "yahoo", datetime(2014,1,1))
gluu = web.DataReader("GLUU", "yahoo", datetime(2014,1,1))
twtr = web.DataReader("twtr", "yahoo", datetime(2014,1,1))
sbux = web.DataReader("sbux", "yahoo", datetime(2010,11,10),datetime(2010,12,28))
print znga.head()

#pk.dump(znga, open( "znga.p", "wb" ))
#pk.dump(gluu, open( "gluu.p", "wb" ))


#znga2 = pk.load( open( "znga.p", "rb" ) )

#print znga2

z = znga['Adj Close'].sum()
g = gluu['Adj Close'].sum()
zz = znga['Adj Close'].mean()
gg = gluu['Adj Close'].mean()
d = {'ratio':znga['Adj Close']/gluu['Adj Close'],'znga': znga['Adj Close'], 'gluu': gluu['Adj Close']}
both = pd.DataFrame(data = {'znga': znga['Adj Close'], 'gluu': gluu['Adj Close']})
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

print d

d['ratio'].plot(style='ro')
plt.ylabel('znga/gluu', fontsize=16)
plt.axhline(y=d['ratio'].mean(),color='r',ls='--')
plt.axhline(y=d['ratio'].mean()-d['ratio'].std(),color='b',ls='--')
plt.axhline(y=d['ratio'].mean()+d['ratio'].std(),color='b',ls='--')
plt.show()
#print both.corr(method='pearson')
#print both.corr(method='kendall')
#print both.corr(method='spearman')



