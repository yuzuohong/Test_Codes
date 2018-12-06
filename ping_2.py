import os
import time
import csv
import numpy as np

csvfile = 'hosts.csv'

# read the csv sheet into a numpy array
with open(csvfile,'r') as file:
    raw_data = csv.reader(file,delimiter='\t')
    data = [d for d in raw_data]
data_array = np.asarray(data)

# define the checking function
def check(hostname,instance):
    response = os.system('ping -n 1 -l 1 ' + hostname) #PING command
    if response == 0: #packet received successfully
        up_message = ('Instance ' \
                       + instance \
                       + ' is UP')
        print(up_message)
    else: #packet lost
        down_message = ('Instance '\
                       + instance\
                       + ' is DOWN!!! at '\
                       + time.strftime('%Y.%m.%d %H.%M.%S'))
        print('*********************')
        print(down_message)
        print('*********************')

try:
    while True:
        print('ICMP Checking starts at ' + time.strftime('%Y.%m.%d %H.%M.%S'))
        for i in range(len(data_array)):
            host = data_array[i][0] #read the first column into host list
            sap_instance = data_array[i][1] #read the second column into instance list
            check(host,sap_instance) #call the checking function
            time.sleep(0.1)

except KeyboardInterrupt:
    print('Checking is cancelled with user interruption')
