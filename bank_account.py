class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print('You cannot deposit negative amount')
        else:
            self.balance += amount
            print(f'Depositing {amount} to {self.owner}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            print(f'Withdrawing {amount} from {self.owner}')

    def show_balance(self):
        print(f'Balance: {self.balance}')

account = BankAccount('Nick', 1000)
account.deposit(0)
account.withdraw(100)
account.show_balance()
print(f'You deposited 100, balance is now {account.balance}')
print(f'You have {account.balance} balance.')

