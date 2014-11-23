import pandas as pd
import pandas.io.data as web
from datetime import datetime
from pandas.tseries.offsets import BDay
import random as random


today = pd.datetime.today() - BDay(1 + random.randint(0,100))  

stock = ["X","GOOG", "T", "YHOO", "ORCL", "IBM", "BA", "AMZN","JNJ","C"]
index = ["X","GOOG", "T", "YHOO", "ORCL", "IBM", "BA", "AMZN","JNJ","C"]


iret = []
for y in stock:
    price = web.DataReader(y, "yahoo", today - BDay(10),today)
    z = price.at[price.index[10],'Close'] - price.at[price.index[0],'Close'] 
    iret.append(z)    


ret = []

for x in range(10):
    front = today - BDay(9 + x) 
    behind = front - BDay(1)
    #print front
    #print behind
    pret = []
    for y in stock:
       #print y
       price = web.DataReader(y, "yahoo", behind,front)
       #print price.head()
       x = price.at[price.index[1],'Close'] - price.at[price.index[0],'Close'] 
       #print x
       pret.append(x)
      
    a = max(pret) 
    ret.append(a)
    i = pret.index(a)
    stock.pop(i)

print sum(ret)
print sum(iret)/10.

