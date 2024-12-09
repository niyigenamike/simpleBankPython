class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance):
        self.__account_number = account_number  # Private attribute
        self.__account_holder = account_holder  # Private attribute
        self.__balance = initial_balance  # Private attribute

    @property
    def balance(self):
        """Getter for balance - allows read access to balance."""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter for balance - allows controlled modification of balance."""
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative")

    @property
    def account_holder(self):
        """Getter for account holder - allows read access to account holder."""
        return self.__account_holder

    @account_holder.setter
    def account_holder(self, name):
        """Setter for account holder - allows controlled modification of account holder name."""
        if name:
            self.__account_holder = name
        else:
            raise ValueError("Account holder name cannot be empty")

    def deposit(self, amount):
        """Public method to deposit money into the account."""
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        """Public method to withdraw money from the account."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient funds or invalid amount")

    def get_account_info(self):
        """Public method to get account information."""
        return f"Account Number: {self.__account_number}, Account Holder: {self.__account_holder}, Balance: {self.__balance}"


# Creating a BankAccount object
account = BankAccount("123456789", "John Doe", 1000)

# Accessing private data through getters
print(account.balance)  # Output: 1000
print(account.account_holder)  # Output: John Doe

# Modifying private data through setters
account.balance = 1500
print(account.balance)  # Output: 1500

account.account_holder = "Jane Doe"
print(account.account_holder)  # Output: Jane Doe

# Performing transactions
account.deposit(500)
print(account.balance)  # Output: 2000

account.withdraw(300)
print(account.balance)  # Output: 1700

# Accessing account info
print(account.get_account_info())  # Output: Account Number: 123456789, Account Holder: Jane Doe, Balance: 1700

# Attempting to set invalid values
try:
    account.balance = -100  # Raises ValueError: Balance cannot be negative
except ValueError as e:
    print(e)

try:
    account.account_holder = ""  # Raises ValueError: Account holder name cannot be empty
except ValueError as e:
    print(e)
