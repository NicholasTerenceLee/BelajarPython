class Bank:
    def __init__(self, owner, bankacc):
        self.owner = owner
        self.bankacc = bankacc

    def deposit(self, amount):
        self.bankacc += amount
        print('Your current balance is : ', self.bankacc)

    def withdraw(self, amount):
        self.bankacc -= amount
        if self.bankacc < 0:
            print("Your balance is not enough, please try next time")
            self.bankacc += amount
        else:
            print("Your current balance is : ", self.bankacc)


x = input("What is your name? : ")

p1 = Bank(x, 500000)

print('Hello Sir/Lady', p1.owner)
print("What would you like to do? ")
print('a.) Deposit')
print('b.) Withdraw')
print('c.) None')
y = input('Choice [a/b/c]: ')

if y == 'a':
    z = float(input('How Much? : '))
    p1.deposit(z)

elif y == 'b':
    z = float(input('How Much? : '))
    p1.withdraw(z)

elif y == 'c':
    print('OK')

else:
    print('What?')
