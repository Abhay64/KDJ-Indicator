# KDJ-Indicator
KDJ indicator is an extension of Stochastic oscillator. KDJ has been developed from Stochastic Oscillator and includes one more ‘J’ line along with the traditional ‘D’ and ‘K’ lines.
# Prequisites
* Python 3.6.4
* numpy
* panda
* matplotlib
# What is KDJ Indicator
KDJ indicator is a technical indicator used to analyze and predict changes in stock trends and price patterns in a traded asset. KDJ indicator is otherwise known as the random index. It is a very practical technical indicator which is most commonly used in market trend analysis of short-term stock. KDJ is a derived form of the Stochastic Oscillator Indicator with the only difference of having an extra line called the J line.
# How it Works
The formula compares the current close to the low, high and range of a set period and then creates two lines, %K and %D. %K is the faster line, %D is simply a moving average of %K and provides a signal line. The KDJ adds a third line, the %J, for a total of three; %K%D%J, KDJ. The %J line is nothing more than the difference between the other two lines, very similar to MACD. The big difference between %J and MACD is one, it isn’t presented as a histogram and two, the two figures are weighted giving more emphasis on the shorter term %K line. This creates a line that moves very slowly and has the ability to move outside the range of the typical stochastic indicator. Stochastic ranges between 0 and 100, KDJ can move outside this range and that movement is one of the signals it can give.

It works a lot like regular stochastic but because it is so slow it is a bit of a lagging indicator. The most common signals it gives is based on where %J is in the range. If it is between 20 and 80 the market is neutral, if it is above 80 it is bullish/overbought and if it is below 20 it is bearish/oversold. If it is below or above 0 or 100 it is very bearish or very bullish, but also very-oversold and very-overbought, so you have to be careful. These lines are used for crossovers in either direction but best used in line with the the trend.
# Mathematical Description
KDJ is calculated quite alike Stochastic indicator, but the difference is in having a J line, which Stochastic does not have.
* The %K line is calculated the following way:
<p align="center"> 
<img src="https://static.anychart.com/images/technical_indicators/kdj1.png"></p>

Where pK is the first period that is set through the stochastic() method, which is a period for the %K value.
* To create the %D line, use the next formula:
<p align="center"> 
<img src="https://static.anychart.com/images/technical_indicators/kdj2.png"></p>

Where p3 is the third period that is set through the stochastic() method, which is a period for the %D value.
* This is how the %J line is calculated:
<p align="center"> 
<img src="https://user-images.githubusercontent.com/26857440/38862045-91cb138a-4251-11e8-918a-d1ab75867695.PNG"></p>

# Implementing KDJ Indicator
**Importing Data**
```python
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df = pd.read_csv('Put Your CSV File Here!!!')
# converting from UNIX timestamp to normal
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
```
**Finding Highest Values within k Periods**
```python
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
```
**Finding Lowest Values within k Periods**
```python
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
  # skip one from starting after each iteration
	y=y-(kperiods-1)
print("Lowest array size",len(array_lowest))
print(array_lowest)
```
**Finding %K Line Values**
```python
#KDJ (K line, D line, J line)
Kvalue=[]
for x in range(kperiods,array_close.size):
   k = ((array_close[x]-array_lowest[x-kperiods])*100/(array_highest[x-kperiods]-array_lowest[x-kperiods]))
   Kvalue.append(k)
print(len(Kvalue))
print(Kvalue)
```
**Finding %D Line Values**
```python
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
	# d values for %d line adding in the list Dvalue
	Dvalue.append(mean)
    # skip one from starting after each iteration
	y=y-(dperiods-1)
print(len(Dvalue))
print(Dvalue)
```
**Finding %J Line Values**
```python
Jvalue=[None,None]
for x in range(0,len(Dvalue)-dperiods+1):
	j=(Dvalue[x+2]*3)-(Kvalue[x+2]*2)
	# j values for %j line
	Jvalue.append(j)
print(len(Jvalue))
print(Jvalue)
```
**Output**
```python
# Visualising the result
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
```
<p align="center"> 
<img src="https://user-images.githubusercontent.com/26857440/38863468-59d12a9c-4255-11e8-915d-7d52f66662e8.PNG"></p>

# References
* [Mathematical Description](https://docs.anychart.com/Stock_Charts/Technical_Indicators/Mathematical_Description#kdj) AnyChart
* [Theoretical Explanation](https://www.thatsucks.com/kdj-stochastic-indicator-can-you-improve-on-perfection/) That Sucks
* [Stochastic Oscillator](http://investexcel.net/how-to-calculate-the-stochastic-oscillator/) Investexcel
* [KDJ Indicator](http://www.tradewithtrend.com/amibroker-afl-kdj-indicator/) TradeWithTrend