import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math
from randWalk import randWalk

#############################################################################
#Author: Tony Sanchez
#Last edited: 10-14-2018
#Last editor: Tony Sanchez
#Description:
#This function generates FAKED data in the same format that's used in Plot.py
#use this f(x) gen to check the accuracy of your algorithms agaist functions 
#that can be easily verrified.
# 
#The API returns real data in the format :
#symbol,open,high,low,price,volume,latestDay,previousClose,change,changePercent
#getStock.py adds a date-time stamp at the end of our real data
#
#This appends a value of x at the end that DOES NOT appear in real data
#############################################################################



#open a file  named GenData.txt
file ='GenData.txt'
out = open(file,"w")

out.write("symbol,price,callTime\n") # write headers so that StockDataset can find the data

#makes arrays
Dates=[]
Prices=[]
x=0
# make up some data
for x in range(1000):
     #sets the date stamp for the test signal data
     date = (datetime.datetime.utcnow() + datetime.timedelta(seconds =x)).strftime("%H:%M:%S")
     
     #your test signal function goes here:
#     price = x**(2)#+20*x*math.sin(x/math.pi)
     
     # for random walk: (comment out test function above first)
     price = randWalk(x, Prices)

          
     Dates.append(date)
     Prices.append(price) 

     out.write('FAKE,'+str(price)+','+str(date)+'\n')
     
#     out.write("symbl,open,high,low, ")
#     out.write(str(price)+", vol,Day,prevCls,diff,diff%, ")
#     out.write(str(date)+", ")
#     out.write(str(x)+ "\n") # for trace tables
## plot
#plt.plot([],[])
#plt.scatter(Dates,Prices,s=8)
## beautify the x-labels
#plt.gcf().autofmt_xdate()

## For Troy's Raspberry Pi
plt.plot(Prices)

##print (Dates)
##print (Prices)

plt.show()
out.close()


