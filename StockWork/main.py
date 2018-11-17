#Author: Idris El
#Last edited by: Troy Maloney
#Last edited date: 10/28/2018
#
#python 3.7
#

from getStockCSV import get_stock_CSV
from parseStockCSV import parse_stock_csv
#from Plot import plot_stocks

import time
import os

def main():
    
    loopCount=0
    sleepCount=0

    stock = input("What stock would you like information about? : ").upper()
    maxLoop = int(input("For how many minutes should I run?\n(enter 390 for a full day) : ") )
    
    now = time.time()   # get the time
    while loopCount < maxLoop:
        elapsed = time.time()       #sets elapsed to current time
        get_stock_CSV(stock)        #API funtion call
        killer = parse_stock_csv(stock)     #Parsing function call
        loopCount=loopCount+1               #loop increment
        elapsed = time.time()-elapsed       #sets elapsed time to loop duration 
        print("Loop iteration: {}".format(loopCount))
        if killer:      # True = error  
            break
        
        if loopCount != maxLoop:
            sleepCount = sleepCount+1
            time.sleep(60.-elapsed)
             
    now = time.time()- now          #sets now to the main.py run time
    os.remove(stock+"stockData.txt") # deletes temp file

    print("Total function run time: {:.3f} seconds".format(elapsed))
    print("Program run time total: {:.3f} seconds".format(now))
    print("Total times looped: {} times.".format(loopCount))
    print("Total times sleep called: {} times.".format(sleepCount))

    print("")
#    Prices = plot_stocks(stock)
    
    
#IF __name__ not needed for python 3 and up, just a hold over XP
if __name__ == "__main__":   
    main()


