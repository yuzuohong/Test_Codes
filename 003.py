REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''
bottles_of_beer = 9
while bottles_of_beer > 1:
    print (REFRAIN % (bottles_of_beer, bottles_of_beer,
        bottles_of_beer - 1))
    bottles_of_beer -= 1


class BankAccount(object):
    def __init__(self, initial_balance=0):
       self.balance = initial_balance
    def deposit (self, amount):
       self.balance += amount
    def withdraw (self, amount):
       self.balance -= amount
    def overdrawn (self):
       return self.balance < 0
my_account = BankAccount(15)
my_account.withdraw(5)
print (my_account.balance)

