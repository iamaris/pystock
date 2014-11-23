import pandas as pd
import pandas.io.data as web
from pandas.tseries.offsets import BDay
import time

today = pd.datetime.today() - BDay(1) 
yesterday = today - BDay(90)

nyse = ["AMX"]

for stock in nyse:
    price = web.DataReader(stock, "yahoo", yesterday,today)
    print price.head()
    #print price.at[price.index[0],'High']
    #print price.at[price.index[0],'Low']
    #print price.at[price.index[1],'High']
    #print price.at[price.index[1],'Low']
    #if len(price.index)==2:
    #    if price.at[price.index[0],'High'] >  price.at[price.index[1],'High']:
    #        if price.at[price.index[0],'Low'] <  price.at[price.index[1],'Low']:
    #            print stock, price.at[price.index[1],'High'], price.at[price.index[1],'Low']
    #time.sleep(30) # delays for 5 seconds



