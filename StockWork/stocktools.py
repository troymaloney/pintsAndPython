
import csv
import os
import glob

class StockDataset:
    """
    Metadata is the column headers stored in *stockData.txt file
    """

    def __init__(self, data_dir, verbose=True):

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
        
#        self.headers = []
        
        with open(headers_fname, 'r') as headers_file:
            headers_reader = csv.reader(headers_file, delimiter=',')
            
            self.headers = next(headers_reader)
            
        


## FOR TESTING -- COMMENT or DELETE in release ##
cron_dataset = StockDataset('/home/pi/Documents/pintsAndPython/StockWork/sample_data')

print(cron_dataset.headers)
