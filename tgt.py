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
#time.sleep(5) # delays for 5 seconds
#today = pd.datetime.today() 
today = pd.datetime.today() 
yesterday = today  - BDay(5000) 

#p = web.DataReader("SPY", "yahoo",yesterday,today)
p = web.DataReader("YELP", "yahoo",yesterday,today)

#print p.head()
#print p.tail()
#print len(p)

N = 0
Np = 0
Nm = 0
Cp = 0
Cm = 0
profitup = 0.0
profitdown = 0.0
loss = 0.0
for i in range(len(p)-1):
    if p.at[p.index[i+1],'Open'] >  p.at[p.index[i],'High']:
        #print "Gap up!"
        Np = Np + 1
        if p.at[p.index[i+1],'Low'] <=  p.at[p.index[i],'High']:
            Cp = Cp + 1
    if p.at[p.index[i+1],'Open'] <  p.at[p.index[i],'Low']:
        #print "Gap down!" 
        Nm = Nm + 1
        if p.at[p.index[i+1],'High'] >=  p.at[p.index[i],'Low']:
            Cm = Cm + 1


print "# Gap + :", Np
print "# Gap + filled :", Cp
print "% Gap + filled :", float(Cp)/float(Np)
print "# Gap - :", Nm
print "# Gap - filled :", Cm
print "% Gap - filled :", float(Cm)/float(Nm)
