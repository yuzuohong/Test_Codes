#range() function test

for i in range(0,500,30):
	print(i)


#indices of a sequence

name_list = ['Mary','Ellen','Jessica','Lily']
for i in range(len(name_list)):
	print('No.',i+1,name_list[i])

print(range(10))

print(list(range(0,10)))

for i in range(0,10):
	print('row no.',i+1,'\n')


#break statement

for n in range(2,10):
	for x in range(2,n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		print(n,'is a prime number')#loop fell through without finding a factor

