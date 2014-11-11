import urllib
import pandas as pd
import pandas.io.data as web
#from datetime import datetime
import matplotlib.pyplot as plt
import pickle as pk
from pandas.tseries.offsets import BDay
# pd.datetime is an alias for datetime.datetime
#today = pd.datetime.today() 
import time

time.sleep(5) # delays for 5 seconds
today = pd.datetime.today() - BDay(1) 
yesterday = today - BDay(1)
#print today
#print yesterday 

#tmp = [line.rstrip() for line in open('nyse.list')]
tmp = [line.rstrip() for line in open('nyse.vol')]
#f = open('nyse.list','r')
#nyse = f.readlines()
#f.close()
nyse = []
for line in tmp:
    cleanedLine = line.strip()
    if cleanedLine:
        nyse.append(cleanedLine)
#print nyse

for stock in nyse:
    #print stock
    #price = web.DataReader(stock, "google", yesterday,today)
    price = web.DataReader(stock, "yahoo", yesterday,today)
    #print price.head()
    #print price.at[price.index[0],'High']
    #print price.at[price.index[0],'Low']
    #print price.at[price.index[1],'High']
    #print price.at[price.index[1],'Low']
    if len(price.index)==2:
        if price.at[price.index[0],'High'] >  price.at[price.index[1],'High']:
            if price.at[price.index[0],'Low'] <  price.at[price.index[1],'Low']:
                print stock, price.at[price.index[1],'High'], price.at[price.index[1],'Low'],(price.at[price.index[1],'High']-price.at[price.index[1],'Low'])
    #time.sleep(30) # delays for 5 seconds




#pk.dump(znga, open( "znga.p", "wb" ))
#znga2 = pk.load( open( "znga.p", "rb" ) )
#print znga2
"""
z = znga['Adj Close'].sum()
g = gluu['Adj Close'].sum()
zz = znga['Adj Close'].mean()
gg = gluu['Adj Close'].mean()
d = {'ratio':znga['Adj Close']/gluu['Adj Close'],'znga': znga['Adj Close'], 'gluu': gluu['Adj Close']}
both = pd.DataFrame(data = {'znga': znga['Adj Close'], 'gluu': gluu['Adj Close']})
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

#print both.corr(method='pearson')
#print both.corr(method='kendall')
#print both.corr(method='spearman')



