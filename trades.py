from pandas import read_csv
from urllib import urlopen

#page = urlopen("http://n3rf.com/aris.csv")

df = read_csv("trades.csv")

#print df
#print df['Trigger']

print df.groupby(["Symbol"]).sum()
