from datetime import datetime
class Transaction:
    def __init__(self, amount, narration, transaction_type, balance_after, to_account=None, from_account=None, date=None):
        if amount <= 0:
            print("Transaction failed: amount must be greater than zero.")
            return
        allowed_types = ["deposit", "withdrawal", "loan", "repayment", "interest", "transfer_in", "transfer_out"]
        if transaction_type not in allowed_types:
            print("Transaction failed: invalid transaction type.")
            return
        self.amount = amount
        self.narration = narration
        self.transaction_type = transaction_type
        self.balance_after = balance_after
        self.date = date if date else datetime.now()
        self.to_account = to_account
        self.from_account = from_account
class Account:
    def __init__(self, name):
        self.__name = name
        self.__transactions = []
        self.__loans = 0
        self.__is_frozen = False
        self.__is_closed = False
        self.__min_balance = 100
        self.__account_number = None
    # Protected/private methods
    def __get_current_balance(self):
        if not self.__transactions:
            return 0
        return self.__transactions[-1].balance_after
    def __record_transaction(self, amount, narration, t_type, to_acc=None, from_acc=None):
        new_balance = self.__get_current_balance()
        if t_type in ["deposit", "loan", "interest", "transfer_in"]:
            new_balance += amount
        elif t_type in ["withdrawal", "repayment", "transfer_out"]:
            new_balance -= amount
        tx = Transaction(amount, narration, t_type, new_balance, to_acc, from_acc)
        if tx.amount:  # Only add if valid
            self.__transactions.append(tx)
    # Public methods
    def deposit(self, amount):
        if self.__is_closed:
            print("Account is closed.")
            return
        if self.__is_frozen:
            print("Account is frozen.")
            return
        if amount <= 0:
            print("Deposit must be more than zero.")
            return
        self.__record_transaction(amount, "Deposit", "deposit")
        print(f"{self.__name}, deposit successful. Balance: {self.__get_current_balance()}")
    def withdraw(self, amount):
        if self.__is_closed:
            print("Account is closed.")
            return
        if self.__is_frozen:
            print("Account is frozen.")
            return
        if amount <= 0:
            print("Invalid amount.")
            return
        current_balance = self.__get_current_balance()
        if current_balance - amount < self.__min_balance:
            print("Cannot withdraw. Minimum balance rule violated.")
            return
        self.__record_transaction(amount, "Withdrawal", "withdrawal")
        print(f"{self.__name}, withdrawal successful. Balance: {self.__get_current_balance()}")
    def transfer(self, amount, other_account):
        if self.__is_closed or other_account.__is_closed:
            print("One of the accounts is closed.")
            return
        if self.__is_frozen or other_account.__is_frozen:
            print("One of the accounts is frozen.")
            return
        if not isinstance(other_account, Account):
            print("Invalid target account.")
            return
        current_balance = self.__get_current_balance()
        if current_balance - amount < self.__min_balance:
            print("Transfer would violate minimum balance.")
            return
        self.__record_transaction(amount, f"Transfer to {other_account.__name}", "transfer_out", to_acc=other_account.__name)
        other_account.__record_transaction(amount, f"Transfer from {self.__name}", "transfer_in", from_acc=self.__name)
        print(f"{self.__name}, you transferred {amount} to {other_account.__name}.")
    def get_loan(self, amount):
        if self.__is_closed or self.__is_frozen:
            print("Account is not active.")
            return
        if amount <= 0 or self.__loans + amount > 500:
            print("Loan denied.")
            return
        self.__loans += amount
        self.__record_transaction(amount, "Loan approved", "loan")
        print(f"{self.__name}, loan approved. Balance: {self.__get_current_balance()}")
    def repay_loan(self, amount):
        if self.__loans <= 0:
            print("No loan to repay.")
            return
        repay_amount = min(amount, self.__loans)
        self.__loans -= repay_amount
        self.__record_transaction(repay_amount, "Loan repayment", "repayment")
        print(f"{self.__name}, loan repaid. Loan balance: {self.__loans}")
    def apply_interest(self):
        current_balance = self.__get_current_balance()
        if self.__is_closed or current_balance <= 0:
            print("No interest added.")
            return
        interest = current_balance * 0.05
        self.__record_transaction(interest, "Interest applied", "interest")
        print(f"{self.__name}, interest added. New balance: {self.__get_current_balance()}")
    def show_balance(self):
        print(f"{self.__name}, your balance is {self.__get_current_balance()}")
    def freeze_account(self):
        if self.__get_current_balance() <= 0:
            print("Cannot freeze empty account.")
            return
        self.__is_frozen = True
        print("Account frozen.")
    def unfreeze_account(self):
        self.__is_frozen = False
        print("Account unfrozen.")
    def close_account(self):
        if self.__get_current_balance() == 0 and self.__loans == 0:
            self.__is_closed = True
            print("Account closed.")
        else:
            print("Cannot close account with balance or loan.")
    def get_statement(self):
        print(f"--- {self.__name}'s Statement ---")
        for tx in self.__transactions:
            print(f"{tx.date.strftime('%Y-%m-%d %H:%M:%S')} | {tx.transaction_type.upper()} | {tx.narration} | Amount: {tx.amount} | Balance: {tx.balance_after}")
        print("--------------------------------")
    def view_account_details(self):
        print(f"Owner: {self.__name}")
        print(f"Balance: {self.__get_current_balance()}")
        print(f"Loan: {self.__loans}")
        print(f"Frozen: {self.__is_frozen}")
        print(f"Closed: {self.__is_closed}")
    def set_minimum_balance(self, amount):
        if amount >= 0:
            self.__min_balance = amount
            print(f"Minimum balance set to {amount}")
        else:
            print("Invalid minimum balance.")
    def change_owner(self, new_name):
        old_name = self.__name
        self.__name = new_name
        print(f"Changed account owner from {old_name} to {self.__name}")
    def set_account_number(self, number):
        self.__account_number = number
        print(f"Account number set to {number}")
New
10:02
account_meron = Account("Meron")
account_kidane = Account("Kidane")
print(account_meron.deposit(1000))           # Deposit to Meron
print(account_meron.withdraw(200))           # Withdraw from Meron
print(account_meron.transfer(300, account_kidane))  # Transfer to Kidane
print(account_meron.get_loan(250))           # Get a loan
print(account_meron.repay_loan(100))         # Repay part of the loan
print(account_meron.apply_interest())        # Apply 5% interest
print(account_meron.show_balance())          # Show Meron’s balance
print("\nMeron's Statement:")
print(account_meron.get_statement())
print("\nKidane's Statement:")
print(account_kidane.get_statement())
10:03
from datetime import datetime
class Transaction:
    def __init__(self, amount, narration, transaction_type):
        if amount <= 0:
            print("Error: Amount must be positive.")
            self.amount = 0
        else:
            self.amount = amount
        valid_types = ["DEPOSIT", "WITHDRAWAL", "TRANSFER_IN", "TRANSFER_OUT", "LOAN", "LOAN_REPAYMENT", "INTEREST"]
        if transaction_type not in valid_types:
            print("Error: Invalid transaction type.")
            self.transaction_type = "UNKNOWN"
        else:
            self.transaction_type = transaction_type
        self.narration = narration
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def __str__(self):
        return f"{self.date} | {self.transaction_type} | {self.narration} | Amount: {self.amount}"
class Account:
    def __init__(self, holder_name):
        self.__holder_name = holder_name
        self.__transactions = []
        self.__loan_balance = 0
        self.__is_frozen = False
        self.__is_closed = False
        self.__min_balance = 100
    def __add_transaction(self, transaction):
        if transaction.amount > 0:
            self.__transactions.append(transaction)
    def get_balance(self):
        balance = 0
        for t in self.__transactions:
            if t.transaction_type in ["DEPOSIT", "TRANSFER_IN", "LOAN", "INTEREST"]:
                balance += t.amount
            elif t.transaction_type in ["WITHDRAWAL", "TRANSFER_OUT", "LOAN_REPAYMENT"]:
                balance -= t.amount
        return balance
    def deposit(self, amount):
        if self.__is_closed:
            return "Account is closed."
        if self.__is_frozen:
            return "Account is frozen."
        if amount <= 0:
            return "Deposit amount must be positive."
        tx = Transaction(amount, "Deposit", "DEPOSIT")
        self.__add_transaction(tx)
        return f"{self.__holder_name}, deposit successful. Balance: {self.get_balance()}"
    def withdraw(self, amount):
        if self.__is_closed:
            return "Account is closed."
        if self.__is_frozen:
            return "Account is frozen."
        if amount <= 0:
            return "Invalid withdrawal amount."
        if self.get_balance() - amount < self.__min_balance:
            return "Insufficient funds after maintaining minimum balance."
        tx = Transaction(amount, "Withdrawal", "WITHDRAWAL")
        self.__add_transaction(tx)
        return f"{self.__holder_name}, withdrawal successful. Balance: {self.get_balance()}"
    def transfer(self, amount, recipient):
        if self.__is_closed or self.__is_frozen:
            return "Account is not active."
        if not isinstance(recipient, Account):
            return "Recipient must be an Account."
        if amount <= 0:
            return "Transfer amount must be positive."
        if self.get_balance() - amount < self.__min_balance:
            return "Insufficient funds after transfer."
        self.__add_transaction(Transaction(amount, f"Transfer to {recipient.__holder_name}", "TRANSFER_OUT"))
        recipient.__add_transaction(Transaction(amount, f"Transfer from {self.__holder_name}", "TRANSFER_IN"))
        return f"{self.__holder_name} transferred {amount} to {recipient.__holder_name}."
    def get_loan(self, amount):
        if self.__is_closed or self.__is_frozen:
            return "Account is not active."
        if amount <= 0:
            return "Loan amount must be positive."
        if self.__loan_balance + amount > 500:
            return "Loan limit exceeded."
        self.__loan_balance += amount
        tx = Transaction(amount, "Loan received", "LOAN")
        self.__add_transaction(tx)
        return f"{self.__holder_name}, loan approved. Balance: {self.get_balance()}"
    def repay_loan(self, amount):
        if self.__loan_balance == 0:
            return "No loan to repay."
        if amount <= 0:
            return "Repayment amount must be positive."
        repayment = min(amount, self.__loan_balance)
        self.__loan_balance -= repayment
        tx = Transaction(repayment, "Loan repayment", "LOAN_REPAYMENT")
        self.__add_transaction(tx)
        return f"{self.__holder_name}, repaid {repayment}. Loan balance: {self.__loan_balance}"
    def apply_interest(self):
        if self.__is_closed or self.__is_frozen:
            return "Account is not active."
        if self.get_balance() <= 0:
            return "No interest on zero or negative balance."
        interest = self.get_balance() * 0.05
        tx = Transaction(interest, "Interest added", "INTEREST")
        self.__add_transaction(tx)
        return f"{self.__holder_name}, 5% interest added. Balance: {self.get_balance()}"
    def get_statement(self):
        statement = f"--- {self.__holder_name}'s Statement ---\n"
        for t in self.__transactions:
            statement += str(t) + "\n"
        return statement.strip()
    def show_balance(self):
        return f"{self.__holder_name}, your current balance is {self.get_balance()}"