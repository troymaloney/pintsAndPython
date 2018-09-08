from getStockCSV import get_stock_CSV
from parseStockCSV import parse_stock_csv

import time

def main():
    maxLoop = 10
    loopCount=0
    sleepCount=0
    now = time.time()   # get the time

    stock = input("What stock would you like information about: ")

    while loopCount < maxLoop:
        elapsed = time.time()
        get_stock_CSV(stock)
        killer = parse_stock_csv(stock)
        loopCount=loopCount+1
        elapsed = time.time()-elapsed
        print("Loop iteration: {}".format(loopCount))
        if killer:
            break
        
        if loopCount != maxLoop:
            sleepCount = sleepCount+1
            time.sleep(60.-elapsed)
             
    now = time.time()- now    
    print("Total function run time: {:.43f} seconds".format(elapsed))
    print("Program run time total: {:.3f} seconds".format(now))
    print("Total times looped: {} times.".format(loopCount))
    print("Total times sleep called: {} times.".format(sleepCount))

#IF __name__ not needed for python 3 and up, just a hold over XP
if __name__ == "__main__":
    main()




                 
