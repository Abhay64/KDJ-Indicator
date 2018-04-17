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

* To create the %D line, use the next formula:
<p align="center"> 
<img src="https://static.anychart.com/images/technical_indicators/kdj2.png"></p>

* This is how the %J line is calculated:
<p align="center"> 
<img src="https://user-images.githubusercontent.com/26857440/38862045-91cb138a-4251-11e8-918a-d1ab75867695.PNG"></p>

