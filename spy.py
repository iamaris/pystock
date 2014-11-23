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

#print p.head()
#print p.tail()
#print len(p)

N = 0
Np = 0
Nm = 0
Gp = 0
Gm = 0
Nd = 0
evenp = 0
evenm = 0
profitup = 0.0
profitdown = 0.0
loss = 0.0
for i in range(len(p)-2):
    notworking = 1
    if p.at[p.index[i],'High'] >  p.at[p.index[i+1],'High']:
        if p.at[p.index[i],'Low'] <  p.at[p.index[i+1],'Low']:
            #print p.index[i+1] 
            N = N + 1
            if p.at[p.index[i+2],'Low'] >  p.at[p.index[i+1],'Low']:
                if p.at[p.index[i+2],'Open'] <  p.at[p.index[i+1],'High']:
                    if p.at[p.index[i+2],'Close'] >  p.at[p.index[i+1],'High']:
                        Np = Np + 1
                        #print "+ working"
                        profitup = profitup + (p.at[p.index[i+2],'Close'] - p.at[p.index[i+1],'High'])
                        notworking = 0
            if p.at[p.index[i+2],'High'] <  p.at[p.index[i+1],'High']:                                                
                if p.at[p.index[i+2],'Open'] >  p.at[p.index[i+1],'Low']:                                            
                    if p.at[p.index[i+2],'Close'] <  p.at[p.index[i+1],'Low']:                                       
                        Nm = Nm + 1                                                                                   
                        profitdown = profitdown + (p.at[p.index[i+1],'Low'] - p.at[p.index[i+2],'Close'])
                        #print "- working"
                        notworking = 0
            if p.at[p.index[i+2],'Open'] > p.at[p.index[i+1],'High']:                                                
                #print "Gap up"
                Gp = Gp +1
                notworking = 0
            if p.at[p.index[i+2],'Open'] < p.at[p.index[i+1],'Low']:                                                
                #print "Gap down" 
                Gm = Gm +1
                notworking = 0
            if p.at[p.index[i+2],'High'] < p.at[p.index[i+1],'High']:                                                
                if p.at[p.index[i+2],'Low'] > p.at[p.index[i+1],'Low']: 
                    #print "Double inside day!" 
                    #print p.index[i+1] 
                    Nd = Nd + 1  
                    notworking = 0
            if notworking == 1:
                if ((p.at[p.index[i+2],'High'] -p.at[p.index[i+1],'High'] ) >=  (p.at[p.index[i+1],'High']-p.at[p.index[i+1],'Low'])): 
                    print p.index[i+1]
                    print "break-even"
                    evenp = evenp + 1 
                elif ((p.at[p.index[i+1],'Low'] -p.at[p.index[i+2],'Low'] ) >=  (p.at[p.index[i+1],'High']-p.at[p.index[i+1],'Low'])): 
                    #print p.index[i+1]
                    evenm = evenm + 1 
                else:
                    #loss = loss + (p.at[p.index[i+1],'High']-p.at[p.index[i+1],'Low'])
                    print p.index[i+1]
                    print "loss"

print len(p)
print "Np = ",Np
print "Nm = ",Nm
print "Gp = ",Gp
print "Gm = ",Gm
print "Double = ", Nd
print "evenp =", evenp
print "evenm =", evenm
print "ProfitUp =", profitup
print "ProfitDown =", profitdown
print "loss =", loss
print N
print Np + Nm
print Gp + Gm
