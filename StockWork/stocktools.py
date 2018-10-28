
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
    
    !!! The directory that you pass into StockDataset must contain both
        *stockData.txt and *parsedStockData.txt
    !!! The directory can only contain ONE *stockData and 
        ONE *parsedStockData file for now. 

    
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
    
    METHODS:
    none yet :(
    Let me know if you have any ideas!
    
    PLANNED ATTRIBUTES:
    symbol, open, high, low, previousClose -- since these are the same
        in each data run (as far as I know, correct me if I'm wrong),
        calling these attributes should return a single number or string. 
        
    
    PLANNED FEATURES:
    1. The option to read in data that was taken within a range of dates
        instead of just reading in an entire directory
    2. Read in dirs that contain more than one data text file
    3. A safeguard against data from more than one different stock being 
        read in using symbol tag on each API call
   *4. A better way to call/format the date and time than a big list of
        strings that the user has to manipulate themselves

    """

    def __init__(self, data_dir, verbose=True): #verbose False by default in release

        if data_dir[-1] != os.sep: # make sure separator character is appended to end of
            data_dir += os.sep     # of directroy string 
    
        self.data_dir = data_dir # set attribute to return name of directory
        
        if verbose:
            print("Reading in data from "+self.data_dir)

        headers_fname = glob.glob(data_dir+'*stockData.txt')[0] # get name of file where headers are stored
        dataTable_fname = glob.glob(data_dir+'*parsedStockData.txt')[0]# Get name of file where datatable is stored
        
        if verbose:
            print("Headers file is called "+headers_fname)
            print("Data table file is called "+dataTable_fname)
        
        with open(headers_fname, 'r') as headers_file: 
        # read in "headers" file and sets attribute to return list of data table headers
            headers_reader = csv.reader(headers_file, delimiter=',')
            
            self.headers = next(headers_reader) # only takes first line
        
        dataTable_full = []
        
        with open(dataTable_fname, 'r') as data_file:
        # read in data table file and place in dataTable_full list
            data_reader = csv.reader(data_file, delimiter=',')
            for row in data_reader:
                dataTable_full.append(row)
        
        self.dataTable_full = np.array(dataTable_full) # Set attribute to return full datatable
            
        self.prices = self.dataTable_full[:,4].astype(np.float) # attr to return list of prices
        self.volumes = self.dataTable_full[:,5].astype(np.float)# attr to return list of volumes
        self.changes = self.dataTable_full[:,8].astype(np.float)# attr to return list of changes
        self.calltimes = self.dataTable_full[:,10]# attr to return list of calltimes
        
        
        change_percents = self.dataTable_full[:,9]
        self.change_percents = np.array([float(p.strip('%') ) for p in change_percents] )
        # strip off percent signs and set attr to return list of percent changes


## FOR TESTING -- COMMENT or DELETE in release ##
#cron_dataset = StockDataset('/home/pi/Documents/pintsAndPython/StockWork/sample_data')

#print(cron_dataset.dataTable_full)



