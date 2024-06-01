# Bank Account System: Create a hierarchy of bank accounts
# (e.g., SavingsAccount, PayPalAccount, UnderThePillowAccount)
# where each account has common attributes (e.g., balance, account number) and specific attributes/methods.
# Implement polymorphic methods such as withdrawing or depositing money for each account type.
class BankAccount:
    """
    Base class for all bank accounts.

    Attributes:
    - balance: current account balance.
    - account_number: unique identifier for the account.
    """

    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        """Deposit a given amount into the account."""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """Withdraw a given amount from the account."""
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Insufficient funds or invalid amount."

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}"


class SavingsAccount(BankAccount):
    """
    Class representing a savings account.

    Additional attributes:
    - interest_rate: interest rate for the account.
    """

    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self.interest_rate = interest_rate

    def add_interest(self):
        """Add interest to the balance based on the interest rate."""
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return f"Added interest of ${interest:.2f}. New balance: ${self.balance:.2f}"


class PayPalAccount(BankAccount):
    """
    Class representing a PayPal account.

    Additional attributes:
    - email: email associated with the PayPal account.
    """

    def __init__(self, balance, account_number, email):
        super().__init__(balance, account_number)
        self.email = email

    def __str__(self):
        return f"PayPal Account (Email: {self.email}), {super().__str__()}"


class UnderThePillowAccount(BankAccount):
    """
    Class representing an 'under the pillow' account.

    Note: This is a conceptual account for keeping cash on hand, with no interest or digital tracking.
    """

    def __init__(self, balance, account_number):
        super().__init__(balance, account_number)

    def withdraw(self, amount):
        """Withdraw a given amount from the account with no fees or restrictions."""
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Insufficient funds or invalid amount."


# Example Usage
savings = SavingsAccount(1000, "SA12345", 1.5)
paypal = PayPalAccount(500, "PP67890", "user@example.com")
pillow = UnderThePillowAccount(200, "PILLOW111")

# Perform operations on savings account
print(savings.deposit(200))
print(savings.withdraw(300))
print(savings.add_interest())

# Perform operations on PayPal account
print(paypal.deposit(100))
print(paypal.withdraw(600))  # Will print an error due to insufficient funds

# Perform operations on UnderThePillowAccount
print(pillow.deposit(100))
print(pillow.withdraw(50))

# Display account details
print("\n" + str(savings))
print(str(paypal))
print(str(pillow))
