#Author: Idris El
#Last edited by: Idris El
#Last edited date: 9/6/2018
#
#python 3.7
#
#To run this program you will NEED access to the OS library
#this library SHOULD be included in your python distribution

#
#This function checks to see if the unparsed file exists.
#if it does, it takes a CSV file and removes the header.
#The data is then appended to a new file (or a new file is created)


import os

def parse_stock_csv():
    tempFile = 'ETHstockData.txt'
    permFile = "ETHparsedStockData.txt"

    #Check to see if the file exists, if it does run the rest of the function
    if os.path.isfile(tempFile):
        with open(tempFile) as f:
            #Skip the header line
            next(f)
            line = f.readline()
            #If the file is empty or has no data, dont do anything
            if line == '':
                print("Empty file\n")

            #else, parsed data will go into new/appended file    
            else:
                print(f"Creating or Appending File: {permFile}\n")
                out = open(permFile,"a")
                while line:
                    out.write(line.strip())
                    line = f.readline()
                    
                out.write("\n")
                out.close()
        #Delete the unparsed file because we no longer need it
        #os.remove(tempFile)
     
    else:
        print("File does Not exist\n")
