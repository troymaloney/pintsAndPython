
import csv
import os
import glob

class StockDataset:
    """
        When given a path to a directory containing stock data gathered 
    with main.py, this class will read in the stored data and create a 
    dataset object. This object will have attributes containing the data
    columns. This could help make our plotting, algorithm, and GUI code
    a little less cumbersome. 
    
    !!! The directory that you pass into StockDataset must contain both
        *stockData.txt and *parsedStockData.txt
    !!! The directory can only contain ONE *stockData and 
        ONE *parsedStockData file for now. 

    
    SYNTAX:
    
    stock = StockDataset("/path/to/file") 
    Set 'verbose' option to True to print reccord of actions to terminal
    
    
    ATTRIBUTES:
    
    data_dir = string containing database path
    
    headers = list of the titles of columns contained in data file
    
    
    METHODS:
    
    none yet :(
    Let me know if you have any ideas!
    
    
    PLANNED ATTRIBUTES:
    
    prices, volumes, changes, change_percents, and calltimes will give lists
    (or numpy arrays) containing data from their respective columns
    
    
    PLANNED FEATURES:
    
    1. The option to read in data that was taken within a range of dates
        instead of just reading in an entire directory
    2. Read in dirs that contain more than one data text file
    
    
    """

    def __init__(self, data_dir, verbose=True): #verbose False by default?

        if data_dir[-1] != os.sep:
            data_dir += os.sep
    
        self.data_dir = data_dir
        
        if verbose:
            print("Reading in data from "+self.data_dir)

        headers_fname = glob.glob(data_dir+'*stockData.txt')[0]
        dataTable_fname = glob.glob(data_dir+'*parsedStockData.txt')[0]
        
        if verbose:
            print("Headers file is called "+headers_fname)
            print("Data table file is called "+dataTable_fname)
        
        with open(headers_fname, 'r') as headers_file:
            headers_reader = csv.reader(headers_file, delimiter=',')
            
            self.headers = next(headers_reader)
            
        


## FOR TESTING -- COMMENT or DELETE in release ##
#cron_dataset = StockDataset('/home/pi/Documents/pintsAndPython/StockWork/sample_data')

#print(cron_dataset.headers)
