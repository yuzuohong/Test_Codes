print ('Hi there!')

name = input('What is your name?\n')
print ('Hello, %s.' % name)

friends = ['john', 'pat', 'gary', 'michael']



for i, name in enumerate(friends):

	print ("iteration {iteration} is {name}".format(iteration=i+1, name=name))



parents, babies = (1, 1)

while babies < 100:
    print ('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)


def greet(name1):
    print ('Good morning', name1)

name1 = input('Whom do you want to greet?\n')

greet (name1)


print ('This is a Fibonacci tuple \n')
a, b = (1,1)

while b < 100000:
    print(b)
    a, b = (b, a+b)

