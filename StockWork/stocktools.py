
#Author: Troy Maloney
#Last edited by: Troy Maloney
#Last edited on: 11-17-18

import csv
import os
import glob
import numpy as np

class StockDataset:
    """
        When given a file containing stock data gathered 
    with main.py, this class will read in the stored data and create a 
    dataset object. This object will have attributes containing the data
    columns. This could help make our plotting, algorithm, and GUI code
    a little less cumbersome. 

    
    How to use:
    
    from stocktools import StockDataset
    stock = StockDataset("data.txt")
    
    If data file is not in current working directory, use data_dir keyword
        to specify the directory where data is stored.
        ex: stock = StockDataset("data.txt", data_dir="path/to/file")
        
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
    1. The option to read in multiple data files and string them together
    2. A way to update with current data as API calls happen

    """

    def __init__(self, fname, data_dir=None, verbose=True): #verbose False by default in release

        if not data_dir: # if no directory specified:
            data_dir = os.getcwd() + os.sep # look for datafile in current directory

        else: # if directory is specified 
            if data_dir[-1] != os.sep: # make sure separator character is appended to end of
                data_dir += os.sep     # of directory string 

        dataFile = data_dir + fname
        
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
        
#       Check if data type exists before creating attributes
        if 'symbol' in headers:
            self.symbol = dataTable_full[0][headers.index('symbol')]
        if 'price' in headers:
            self.prices = self.dataTable_full[:,headers.index('price')].astype(np.float)
        if 'volume' in headers:
            self.volumes = self.dataTable_full[:,headers.index('volume')].astype(np.float)
        if 'change' in headers:
            self.changes = self.dataTable_full[:,headers.index('change')].astype(np.float)
        if 'callTime' in headers:
            self.calltimes = self.dataTable_full[:,headers.index('callTime')]
        if 'changePercent' in headers:
            change_percents = self.dataTable_full[:,headers.index('changePercent')]
            self.change_percents = np.array([float(p.strip('%') ) for p in change_percents] )

## FOR TESTING -- COMMENT or DELETE in release ##
#cron = StockDataset('/home/pi/Documents/pintsAndPython/StockWork')
#print(cron.headers)
#print(cron.dataTable_full)

#print(cron.symbol)


