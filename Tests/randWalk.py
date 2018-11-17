
#Author: Troy Maloney
#Last edited: 11-16-2018
#Last editor: Troy Maloney
#Description:
#    Generates fake data using a random walk for use with the 
#    FunctionGen.py script.

from random import randint

def randWalk(x, Prices, sf=100): 
#    x: iteration count for FunctionGen for loop
#    Prices: list of prices created by FunctionGen
#    sf: scale factor. Optional, Change to make prices more realistic.
    
    if x == 0: #set initial value
        init = randint(1,10)
        return init*sf
    
    else:
        #   Simple random walk -- equal probability of staying the
        # same, increasing or decreasing by one scale factor
        roll = randint(1,3) #roll the dice
        if roll == 1: # subtracts one unit
            next = Prices[x-1]/sf - 1
            if next <= 0:# no negative numbers allowed
                next = 0
            
        elif roll == 2:# stays the same
            next = Prices[x-1]/sf
            
        elif roll == 3:# adds one unit
            next = Prices[x-1]/sf + 1
                        
        return next*sf
