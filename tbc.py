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

p = web.DataReader("SPY", "yahoo",yesterday,today)
#p = web.DataReader("YELP", "yahoo",yesterday,today)

#print p.head()
#print p.tail()
#print len(p)
up = 0
down = 0
N = 0
for i in range(len(p)-3):
    if p.at[p.index[i],'Open'] >  p.at[p.index[i],'Close']:
        if p.at[p.index[i+1],'Open'] >  p.at[p.index[i+1],'Close']:
            if p.at[p.index[i+2],'Open'] >  p.at[p.index[i+2],'Close']:
                N = N + 1
                if p.at[p.index[i+3],'Open'] >=  p.at[p.index[i+3],'Close']:
                    down = down + 1
                else:
                    up = up + 1 
                  
print "total = ",N
print "up    = ",up,"(",float(up)/N,")"
print "down  = ",down,"(",float(down)/N,")"

