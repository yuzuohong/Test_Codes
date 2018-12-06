import random

f = open('012_'+str(random.randint(1000,9999))+'.txt','w')

'''
while True:
    participant = input('Participant name > ')

    if participant == 'quit':

        print('Quitting...')
        break

    score = input('Score for ' + participant + '>')
    f.write(participant + ',' + score + '\n')
'''

for i in range(1,100):
    for j in range(1,100):
    
        f.write('line no.' + str(i*j) + '\n')


f.close()
