import time

# runs the API and all other funtions that need to be looped at a maximum of once per minute 
#once per minute. 

n=0
now = time.time()            # get the time
elapsed =0

while True:
    
    print ("heyo")               # do your stuff
    time.sleep(60.-elapsed)     # sleep accordingly so the full iteration takes 1 second
    n=n+1
    elapsed = time.time() - now  # how long was it running?
    if n==1:                      # breaks loop for testing porpoises
        break                    
print (elapsed)    
