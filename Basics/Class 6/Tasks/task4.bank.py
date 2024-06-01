# Create a class called "BankAccount" with attributes for account number and balance.
# Add methods to the BankAccount class for depositing and withdrawing money.
# Create a subclass of BankAccount called "SavingsAccount" with an additional attribute for interest rate.
# Override the BankAccount class's withdraw method in the SavingsAccount subclass to include a fee for each withdrawal.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposition(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Your bank account's balance is: {self.balance}")

    def withdrawal(self, amount):
        if amount <= self.balance:
            print(f"Withdrew {amount}. Your bank's balance is: {self.balance}")
        else:
            print("Insufficient funds! Try again! :( ")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def withdrawal(self, amount):
        withdrawal_fee = 1
        total_withdrawal = amount + withdrawal_fee
        if total_withdrawal <= self.balance:
            self.balance -= total_withdrawal
            print(f"Withdrawal: {amount}. Your bank account's balance is now: {self.balance}")
        else:
            print("Insufficient funds :(")


bank_account = BankAccount("01293", 5000)
bank_account.deposition(1300)
bank_account.withdrawal(1000)

savings_account = SavingsAccount("12345", 100000, 5)
savings_account.deposition(200000)
savings_account.withdrawal(100)