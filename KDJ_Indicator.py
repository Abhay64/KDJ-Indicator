import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
Url_polo = 'http://34.210.192.138:8000/public?keys=command,currencyPair,start,end,period&values=returnChartData,BTC_BCH,1515819652,1515841252,300'
df = pd.read_json(Url_polo)
df['date'] = pd.to_datetime(df['date'],unit='s').dt.date
array_date = np.array(df['date'])
array_close = np.array(df['close'])
array_open = np.array(df['open'])
array_high = np.array(df['high'])
array_low = np.array(df['low'])
array_volume = np.array(df['volume'])
print("High Array size",array_high.size)
print("Low Array size",array_low.size)
print("Open Array size",array_open.size)
print("Close Array size",array_close.size)
y=0
z=0
#kperiods are 14 array start from 0 index
kperiods=13
array_highest=[]
for x in range(0,array_high.size-kperiods):
	z=array_high[y]
	for j in range(0,kperiods):
		if(z<array_high[y+1]):
			z=array_high[y+1]
		y=y+1
	# creating list highest of k periods
	array_highest.append(z)
	y=y-(kperiods-1)
print("Highest array size",len(array_highest))
print(array_highest)
y=0
z=0
array_lowest=[]
for x in range(0,array_low.size-kperiods):
	z=array_low[y]
	for j in range(0,kperiods):
		if(z>array_low[y+1]):
			z=array_low[y+1]
		y=y+1
	# creating list lowest of k periods
	array_lowest.append(z)
	y=y-(kperiods-1)
print(len(array_lowest))
print(array_lowest)

#KDJ (K line, D line, J line)
Kvalue=[]
for x in range(kperiods,array_close.size):
   k = ((array_close[x]-array_lowest[x-kperiods])*100/(array_highest[x-kperiods]-array_lowest[x-kperiods]))
   Kvalue.append(k)
print(len(Kvalue))
print(Kvalue)
y=0
# dperiods for calculate d values
dperiods=3
Dvalue=[None,None]
mean=0
for x in range(0,len(Kvalue)-dperiods+1):
	sum=0
	for j in range(0,dperiods):
		sum=Kvalue[y]+sum
		y=y+1
	mean=sum/dperiods
	# d values for %d line
	Dvalue.append(mean)
	y=y-(dperiods-1)
print(len(Dvalue))
print(Dvalue)
Jvalue=[None,None]
for x in range(0,len(Dvalue)-dperiods+1):
	j=(Dvalue[x+2]*3)-(Kvalue[x+2]*2)
	# j values for %j line
	Jvalue.append(j)
print(len(Jvalue))
print(Jvalue)
plt.figure(figsize=(25,15), dpi=50, facecolor='w', edgecolor='k')
ax = plt.gca() 
plt.plot(Kvalue,color='red',label = '%K line')
plt.plot(Dvalue,color='blue',label = '%D line')
plt.plot(Jvalue,color='green',label = '%J line')
plt.title('KDJ Indicator', fontsize=20)
df['date'] = df['date'].reset_index()
x=df['date'].index
labels = array_date[13:]
plt.xticks(x, labels, rotation = 'vertical')
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(10)
for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontsize(10)
plt.ylabel('KDJ_Values', fontsize=20)
plt.xlabel('Dates', fontsize=15)
plt.legend()
plt.show()