class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print('You cannot deposit negative amount')
        else:
            self.balance += amount
            self.transactions.append(f'Deposited {amount}')
            print(f'Depositing {amount} to {self.owner}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            self.transactions.append(f'Withdrew {amount}')
            print(f'Withdrawing {amount} from {self.owner}')

    def show_balance(self):
        print(f'Balance: {self.balance}')

    def show_transactions(self):
        print(f'Transactions:')
        for transaction in self.transactions:
            print(f' - {transaction}')

class Savings_Account(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self, rate):
        interest = self.balance * (rate / 100)
        self.balance += interest
        self.transactions.append(f'Added {interest} to {self.owner}')
        print(f'Added {interest} to {self.owner}')

account = Savings_Account('Nick', 1000, 5)
account.deposit(100)
account.withdraw(500)
account.show_balance()
account.show_transactions()
account.add_interest(5)
print(f'You deposited 100, balance is now {account.balance}')
print(f'You have {account.balance} balance.')
