
#Author: Troy Maloney
#Last edited by: Troy Maloney
#Last edited on: 11-17-18


import csv
import os
import glob
import numpy as np

class StockDataset:
    """
        When given a path to a directory containing stock data gathered 
    with main.py, this class will read in the stored data and create a 
    dataset object. This object will have attributes containing the data
    columns. This could help make our plotting, algorithm, and GUI code
    a little less cumbersome. 
    
    !!! Only a directory with ONE data text file can be passed into this 
        class right now

    
    SYNTAX:
    stock = StockDataset("/path/to/file") 
    Set 'verbose' option to True to print record of actions to terminal
    
    
    ATTRIBUTES:
    data_dir = string containing database path
    headers = list of the titles of columns contained in data file
    dataTable_full = the entire data table in a numpy array
    prices = all prices in a 1-d numpy array (list)
    volumes = all volumes in a 1-d numpy array
    changes = all changes in a 1-d numpy array
    calltimes = the date and time of all API calls in string form
    change_percents = all change percentages in a 1-d numpy array
    symbol = returns stock symbol
    
    METHODS:
    none yet :(
    Let me know if you have any ideas!
    
    PLANNED ATTRIBUTES:
    open, high, low, previousClose -- since these are the same
        in each data run (as far as I know, correct me if I'm wrong),
        calling these attributes should return a single number or string. 
        
    
    PLANNED FEATURES:
    1. The option to read in data that was taken within a range of dates
        instead of just reading in an entire directory
    2. Read in dirs that contain more than one data text file
    3. A safeguard against data from more than one different stock being 
        read in using symbol tag on each API call

    """

    def __init__(self, data_dir, verbose=True): #verbose False by default in release

        if data_dir[-1] != os.sep: # make sure separator character is appended to end of
            data_dir += os.sep     # of directroy string 
    
        self.data_dir = data_dir # set attribute to return name of directory
        
        if verbose:
            print("Reading in data from "+self.data_dir)
        
        # Grab only the first stock data file in the directory for now
        dataFile = glob.glob(data_dir+'*parsedStockData.txt')[0]
        
        if verbose:
            print("Data table file is called "+dataFile)
        
        with open(dataFile, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            
            headers = next(reader)
            
            dataTable_full = []
            for row in reader:
                dataTable_full.append(row)
                
        self.dataTable_full = np.array(dataTable_full)
        self.headers = headers
        self.symbol = dataTable_full[0][0]
        
        self.prices = self.dataTable_full[:,headers.index('price')].astype(np.float)
        self.volumes = self.dataTable_full[:,headers.index('volume')].astype(np.float)
        self.changes = self.dataTable_full[:,headers.index('change')].astype(np.float)
        self.calltimes = self.dataTable_full[:,headers.index('callTime')]
        
        change_percents = self.dataTable_full[:,headers.index('changePercent')]
        self.change_percents = np.array([float(p.strip('%') ) for p in change_percents] )

## FOR TESTING -- COMMENT or DELETE in release ##
#cron = StockDataset('/home/pi/Documents/pintsAndPython/StockWork')
#print(cron.headers)
#print(cron.dataTable_full)

#print(cron.symbol)


