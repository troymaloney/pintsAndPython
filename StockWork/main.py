from getStockCSV import get_stock_CSV
from parseStockCSV import parse_stock_csv

import time

def main():
    maxLoop = 5
    loopCount=0
    sleepCount=0
    now = time.time()   # get the time

    while loopCount < maxLoop:
        elapsed = 0
        get_stock_CSV()
        parse_stock_csv()
        loopCount=loopCount+1
        print(f"Loop iteration: {loopCount}")
        if loopCount != maxLoop:
            sleepCount = sleepCount+1
            time.sleep(60.-elapsed)
            
        elapsed = time.time() - now  
        
    print("Program run time: {:.4f} seconds".format(elapsed))
    print(f"Total times looped: {loopCount} times.")
    print(f"Total times sleep called: {sleepCount} times.")

#IF __name__ not needed for python 3 and up, just a hold over XP
if __name__ == "__main__":
    main()




                 
