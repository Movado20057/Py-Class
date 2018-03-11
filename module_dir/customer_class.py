class customer ():
    def __init__(self, name):
        self.name = name

    def set_balance (self, balance):
        self.balance = balance
        return None

    def deposit(self, amount):
        self.balance += amount
        return self.balance 

    def withdraw(self, amount):
        if not amount > self.balance:
            self.balance -= amount
        else:
            raise RuntimeError ("Insufficient Balance")
        return self.balance

    def get_balance (self):
        return self.balance

new_customer = customer ("Seun")
new_customer.set_balance (25000)
print (new_customer.get_balance())
new_customer.deposit(45000)
print (new_customer.get_balance())
new_customer.withdraw(30000)
print (new_customer.get_balance())
