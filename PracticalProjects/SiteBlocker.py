import time, re
from datetime import datetime as dt

hosts_temp = 'hosts'
hosts_path = r'/home/stuart/hosts' # the 'r' escapes escape characters
redirect = '127.0.0.1'

sites_to_block = ['www.facebook.com', 'facebook.com', 'cupofcode01.com', 'www.gmail.com']

#print(dt.now())
#print(dt.today().weekday())
if 9 < dt.now().hour < 17 and dt.today().weekday() < 5:
    print("its working hours")

    with open(hosts_path,'r+') as file:
        content = file.read()   # loads the contents of the file to the variable
        for site in sites_to_block:
            if site in content:                         # check if site already listed
                pass
            else:
                file.write(redirect+' '+site+'\n')      # writing to the file

else:
    print("Time for fun!!")
    file = open(hosts_path,'r+')
    content = file.readlines()                          # read the lines into content
    file.seek(0)                                        # put the cursor at the beginning of the file
    for line in content:
        if not any(site in line for site in sites_to_block):
            file.write(line)                            # write lines back to file

    file.truncate()                                     # blank the end of the file
    print("Time for fun!!")
