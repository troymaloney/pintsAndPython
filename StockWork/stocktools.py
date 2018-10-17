
import csv

class StockDataset:

    def __init__(self, file_name):
    
        with open (file_name) as csvfile:
          readcsv =csv.reader(csvfile,delimiter=',')



