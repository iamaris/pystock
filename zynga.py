import urllib
import pandas as pd
import pandas.io.data as web
from datetime import datetime
import matplotlib.pyplot as plt

znga = web.DataReader("ZNGA", "yahoo", datetime(2014,1,1))
gluu = web.DataReader("GLUU", "yahoo", datetime(2014,1,1))
print znga.head()
z = znga['Adj Close'].sum()
g = gluu['Adj Close'].sum()
zz = znga['Adj Close'].mean()
gg = gluu['Adj Close'].mean()
both = pd.DataFrame(data = {'znga': znga['Adj Close'], 'gluu': gluu['Adj Close']})
both_m = pd.DataFrame(data = {'znga': znga['Adj Close']/zz, 'gluu': gluu['Adj Close']/gg})
both_ret = both.pct_change()
print both_ret.head()
both.plot()
both_m.plot()
both_ret.plot()
plt.show()
