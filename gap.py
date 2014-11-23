import pandas as pd
import pandas.io.data as web
from pandas.tseries.offsets import BDay
import numpy as np
from scipy.stats import itemfreq
today = pd.datetime.today() 
yesterday = today  - BDay(5000) 
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)

def hist(x):
    if (x>=1.0):
       y = 1.05
    else:
       y = x
    return (y//0.05)*0.05


class stock(object):

    def __init__(self, stock="SPY", start=pd.datetime.today() - BDay(5000), end=pd.datetime.today()): 
        self.Ticker = stock 
        self.Start  = start
        self.End    = end 
        self.Np = 0#number of gap up
        self.Nm = 0#number of gap down
        self.Cp = 0#number of filled gap up 
        self.Cm = 0#number of filled gap down
        self.unfilledp = []#ranges of unfilled gap up
        self.unfilledp_percent = []#% relative to previous day range 
        self.filledp = []#ranges of unfilled gap up
        self.filledp_percent = []#% relative to previous day range 
        self.unfilledm = []#ranges of unfilled gap donw
        self.unfilledm_percent = []#% relative to previous day range
        self.filledm = []#ranges of unfilled gap donw
        self.filledm_percent = []#% relative to previous day range

    def findGaps(self):
        p = web.DataReader(self.Ticker, "yahoo",self.Start,self.End)
        for i in range(len(p)-1):
            drange =   p.at[p.index[i],'High'] -  p.at[p.index[i],'Low']
            if p.at[p.index[i+1],'Open'] >  p.at[p.index[i],'High']:
                #"Gap up!"
                gap = float(p.at[p.index[i+1],'Open'] -  p.at[p.index[i],'High'])
                self.Np += 1
                if p.at[p.index[i+1],'Low'] <=  p.at[p.index[i],'High']:
                    #Filled
                    self.Cp += 1
                    self.filledp.append((p.index[i+1],gap))
                    self.filledp_percent.append(float(gap/drange))
                else:
                    #Unfilled
                    self.unfilledp.append((p.index[i+1],gap))
                    self.unfilledp_percent.append(gap/drange)
            if p.at[p.index[i+1],'Open'] <  p.at[p.index[i],'Low']:
                #"Gap down!" 
                gap = float(p.at[p.index[i],'Low'] -  p.at[p.index[i+1],'Open'])
                self.Nm += 1
                if p.at[p.index[i+1],'High'] >=  p.at[p.index[i],'Low']:
                    #Filled
                    self.Cm += 1
                    self.filledm.append((p.index[i+1],gap))
                    self.filledm_percent.append(float(gap/drange))
                else:
                    #Unfilled
                    self.unfilledm.append((p.index[i+1],gap))
                    self.unfilledm_percent.append(gap/drange)

    def generateHist(self):
        temp = []
        for x in self.unfilledp_percent:
            temp.append(hist(x))
 
        up = np.array(temp)
        print "unfilled:"
        print itemfreq(up)

        ftemp = []
        for x in self.filledp_percent:
           ftemp.append(hist(x))

        fup = np.array(ftemp)
        print "filled:"
        print itemfreq(fup)



    def printStats(self):
        print "# Gap + :", self.Np
        print "# Gap + filled :", self.Cp
        print "% Gap + filled :", float(self.Cp)/float(self.Np)
        print "# Gap - :", self.Nm
        print "# Gap - filled :", self.Cm
        print "% Gap - filled :", float(self.Cm)/float(self.Nm)
        print "Minimun range of unfilled gap up:",min(self.unfilledp),"(",min(self.unfilledp_percent),")"
        print "Minimun range of unfilled gap down:",min(self.unfilledm),"(",min(self.unfilledm_percent),")"
        print "Maximum range of unfilled gap up:",max(self.unfilledp),"(",max(self.unfilledp_percent),")"
        print "Mamimum range of unfilled gap down:",max(self.unfilledm),"(",max(self.unfilledm_percent),")"

