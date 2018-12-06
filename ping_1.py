import os
import time
import pandas as pd
from termcolor import colored

csvfile = 'hosts.csv'

# read the csv sheet into a pandas array
df = pd.read_csv(csvfile, sep=',', header=None)


# define the checking function
def check(hostname, instance):
    response = os.system('ping -c 1 -s 1 ' + hostname)
    if response == 0:
        down_message = ('ICMP Checking - Instance ' \
                        + instance \
                        + ' is UP')
        print(down_message)
    else:
        down_message = ('ICMP Checking - Instance ' \
                        + instance \
                        + ' is DOWN!!! at ' \
                        + time.strftime('%Y.%m.%d %H.%M.%S'))
        print(colored('*********************', 'red'))
        print(colored(down_message), 'red')


try:
    while True:
        print('ICMP Checking starts at ' + time.strftime('%Y.%m.%d %H.%M.%S'))
        for i in range(len(df)):
            host = df[0][i]  # read the first column into host list
            sap_instance = df[1][i]  # read the second column into instance list
            check(host, sap_instance)  # call the checking function
            time.sleep(1)

except KeyboardInterrupt:
    print('Checking is cancelled by user interruption')
