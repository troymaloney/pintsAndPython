
import csv
import os
import glob

class StockDataset:

    def __init__(self, data_dir, verbose=True):

        if data_dir[-1] != os.sep:
            data_dir += os.sep
    
        self.data_dir = data_dir
        
        if verbose:
            print("Reading in data from "+self.data_dir)

        metadata_fname = glob.glob(data_dir+'*stockData.txt')[0]
        dataTable_fname = glob.glob(data_dir+'*parsedStockData.txt')[0]
        
        if verbose:
            print("Metadata file is called "+metadata_fname)
            print("Data table file is called "+dataTable_fname)
        
        self.metadata = []
        
        with open(metadata_fname, 'r') as md_file:
            md_reader = csv.reader(md_file, delimiter=',')
            
            for row in md_reader:
                self.metadata.append(row)


## FOR TESTING -- COMMENT or DELETE in release ##
cron_dataset = StockDataset('/home/pi/Documents/pintsAndPython/StockWork/sample_data')
for row in cron_dataset.metadata:
    print(row)
