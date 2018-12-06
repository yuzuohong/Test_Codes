def fib(n):
    '''print a Fibonacci series up to n'''
    a, b = 0, 1
    while a < int(n):
        print(a, '++++++++++')
        a, b = b, a+b
    print()

def fib2(n):
    a, b = 1, 2
    while a < int(n):
        print(a, '***********')
        a, b = b, a*b
    print()

up_to_scope = input('Please input a scope:')

fib(up_to_scope)

fib2(up_to_scope)

f = fib

f2 = fib2

f(up_to_scope)

f2(up_to_scope)
