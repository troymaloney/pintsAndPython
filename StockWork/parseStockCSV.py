#Author: Idris El
#Last edited by: Tony Sanchez
#Last edited date: 10/12/2018
#
#python 3.7
#
#To run this program you will NEED access to the OS library
#this library SHOULD be included in your python distribution

#
#This function checks to see if the unparsed file exists.
#if it does, it takes a CSV file and removes the header.
#The data is then appended to a new file (or a new file is created)
#The function returns a boolean to let the program know if it handled
#a an empty file


import os

def parse_stock_csv(stock):
    tempFile = stock + 'stockData.txt'
    permFile = stock + "parsedStockData.txt"
    killer = False

    #Check to see if the file exists, if it does run the rest of the function
    if os.path.isfile(tempFile):
        with open(tempFile) as f:
            headers = f.readline()
            line = f.readline()
            #If the file is empty or has no data, dont do anything
            #AND send a boolean
            if line == '':
                print("Empty file\n")
                killer = True

            #else, parsed data will go into new/appended file    
            else:
                print("Creating or Appending File: {}".format(permFile))
                out = open(permFile,"a")
                if os.stat(permFile).st_size > 0:
                    while line:
                        out.write(line.strip())
                        line = f.readline()
                else:# write header and then write first line if file is empty
                    while line:
                        out.write(headers.strip()+'\n')
                        out.write(line.strip() )
                        line = f.readline()
                    
                out.write("\n")
                out.close()
     
    else:
        print("File does Not exist\n")
        killer = True
    return killer
