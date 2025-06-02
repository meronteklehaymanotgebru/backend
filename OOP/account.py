from datetime import datetime

class Transaction:
    def __init__(self, amount, narration, transaction_type):
        if amount <= 0:
            print("Error: Amount must be positive.")
            self.amount = 0
        else:
            self.amount = amount
        valid_types = [
            "DEPOSIT", "WITHDRAWAL", "TRANSFER_IN", "TRANSFER_OUT",
            "LOAN", "LOAN_REPAYMENT", "INTEREST"
        ]
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
        self.__account_number = None

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_account_number(self):
        return self.__account_number

    def holder_name(self):
        return self.__holder_name

    def balance(self):
        return self.get_balance()

    def __add_transaction(self, transaction):
        if transaction.amount > 0:
            self.__transactions.append(transaction)

    def get_balance(self):
        balance = 0
        for transaction in self.__transactions:
            if transaction.transaction_type in ["DEPOSIT", "TRANSFER_IN", "LOAN", "INTEREST"]:
                balance += transaction.amount
            elif transaction.transaction_type in ["WITHDRAWAL", "TRANSFER_OUT", "LOAN_REPAYMENT"]:
                balance -= transaction.amount
        return balance

    def deposit(self, amount):
        if self.__is_closed:
            return "Account is closed."
        if self.__is_frozen:
            return "Account is frozen."
        if amount <= 0:
            return "Deposit amount must be positive."
        new_transaction = Transaction(amount, "Deposit", "DEPOSIT")
        self.__add_transaction(new_transaction)
        return f"{self.holder_name()}, deposit successful. Balance: {self.balance()}"

    def withdraw(self, amount):
        if self.__is_closed:
            return "Account is closed."
        if self.__is_frozen:
            return "Account is frozen."
        if amount <= 0:
            return "Invalid withdrawal amount."
        if self.balance() - amount < self.__min_balance:
            return "Insufficient funds after maintaining minimum balance."
        new_transaction = Transaction(amount, "Withdrawal", "WITHDRAWAL")
        self.__add_transaction(new_transaction)
        return f"{self.holder_name()}, withdrawal successful. Balance: {self.balance()}"

    def transfer(self, amount, recipient):
        if self.__is_closed or self.__is_frozen:
            return "Account is not active."
        if not isinstance(recipient, Account):
            return "Recipient must be an Account."
        if amount <= 0:
            return "Transfer amount must be positive."
        if self.balance() - amount < self.__min_balance:
            return "Insufficient funds after transfer."
        outgoing_transaction = Transaction(amount, f"Transfer to {recipient.holder_name()}", "TRANSFER_OUT")
        incoming_transaction = Transaction(amount, f"Transfer from {self.holder_name()}", "TRANSFER_IN")
        self.__add_transaction(outgoing_transaction)
        recipient.__add_transaction(incoming_transaction)
        return f"{self.holder_name()} transferred {amount} to {recipient.holder_name()}."

    def get_loan(self, amount):
        if self.__is_closed or self.__is_frozen:
            return "Account is not active."
        if amount <= 0:
            return "Loan amount must be positive."
        if self.__loan_balance + amount > 500:
            return "Loan limit exceeded."
        self.__loan_balance += amount
        loan_transaction = Transaction(amount, "Loan received", "LOAN")
        self.__add_transaction(loan_transaction)
        return f"{self.holder_name()}, loan approved. Balance: {self.balance()}"

    def repay_loan(self, amount):
        if self.__loan_balance == 0:
            return "No loan to repay."
        if amount <= 0:
            return "Repayment amount must be positive."
        repayment = min(amount, self.__loan_balance)
        self.__loan_balance -= repayment
        repayment_transaction = Transaction(repayment, "Loan repayment", "LOAN_REPAYMENT")
        self.__add_transaction(repayment_transaction)
        return f"{self.holder_name()}, repaid {repayment}. Loan balance: {self.__loan_balance}"

    def apply_interest(self):
        if self.__is_closed or self.__is_frozen:
            return "Account is not active."
        if self.balance() <= 0:
            return "No interest on zero or negative balance."
        interest_amount = self.balance() * 0.05
        interest_transaction = Transaction(interest_amount, "Interest added", "INTEREST")
        self.__add_transaction(interest_transaction)
        return f"{self.holder_name()}, 5% interest added. Balance: {self.balance()}"

    def get_statement(self):
        statement = f"--- {self.holder_name()}'s Statement ---\n"
        for transaction in self.__transactions:
            statement += str(transaction) + "\n"
        return statement.strip()

    def show_balance(self):
        return f"{self.holder_name()}, your current balance is {self.balance()}"

# Example 
account_meron = Account("Meron")
account_meron.set_account_number("1234567890")
print(account_meron.deposit(1000))
print(account_meron.withdraw(200))
print(account_meron.show_balance())
print(account_meron.get_statement())
print(account_meron.get_account_number())