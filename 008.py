def fib(n): #write fibonacci series up to n
        """print a fibonacci series up to n"""
        a, b = 0, 1
        while a < n:
                print(a, end=' \n')
                a, b = b, a + b
        print()

#now call the function we just defined above

up_to = input('Input an integer: ')

fib(int(up_to))

