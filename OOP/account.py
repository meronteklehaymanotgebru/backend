class Account:
    def __init__(self, name):
        self.name = name
        self.deposits = []
        self.withdrawals = []
        self.loans = 0
        self.is_frozen = False
        self.is_closed = False
        self.min_balance = 100 
    def get_balance(self):
        total = 0
        for d in self.deposits:
            total += d
        total_withdraw = 0
        for w in self.withdrawals:
            total_withdraw += w
        return total - total_withdraw
    def deposit(self, money):
        if self.is_closed:
            return "Account is closed."
        if self.is_frozen:
            return "Account is frozen."
        if money > 0:
            self.deposits.append(money)
            return f"{self.name}, your balance now is {self.get_balance()}"
        else:
            return "Deposit must be greater than zero."
    def withdraw(self, money):
        if self.is_closed:
            return "Account is closed."
        if self.is_frozen:
            return "Account is frozen."
        if money <= 0:
            return "Invalid amount"
        if self.get_balance() < money:
            return "Insufficient balance"
        if self.get_balance() - money < self.min_balance:
            return "You can't go below the minimum balance"
        self.withdrawals.append(money)
        return f"{self.name}, you withdrew {money}. Remaining balance: {self.get_balance()}"
    def show_balance(self):
        return f"{self.name}, your current balance is {self.get_balance()}"
    def transfer(self, amount, other_account):
        if self.is_closed:
            return "Account is closed."
        if self.is_frozen:
            return "Account is frozen."
        if amount <= 0:
            return "Transfer amount must be positive."
        if not isinstance(other_account, Account):
            return "Recipient must be an Account object."
        if self.get_balance() < amount:
            return "Not enough balance."
        if self.get_balance() - amount < self.min_balance:
            return "Balance would go below minimum."
        self.withdrawals.append(amount)
        other_account.deposits.append(amount)
        return f"Transfer of {amount} to {other_account.name} successful. Your new balance is {self.get_balance()}"
    def get_loan(self, money):
        if self.is_closed:
            return "Account is closed."
        if self.is_frozen:
            return "Account is frozen."
        if self.loans+money <= 500 and money > 0:
            self.deposits.append(money)
            self.loans += money
            return f"{self.name}, loan approved. New balance: {self.get_balance()}"
        else:
            return "Loan request denied."
    def repay_loan(self, money):
        if self.loans <= 0:
            return "No loan to repay."
        if money <= self.loans:
            self.withdrawals.append(money)
            self.loans -= money
            return f"{self.name}, you have {self.loans} loan left."
        else:
            extra = money - self.loans
            self.withdrawals.append(self.loans)
            self.loans = 0
            return f"{self.name}, loan fully repaid. Extra money: {extra}"
    def get_loan_statement(self):
        return f"{self.name}, your loan balance is {self.loans}"
    def get_statement(self): 
        statement = f"{self.name}'s statement:\nDeposits:\n"
        for d in self.deposits:
            statement += f"  +{d}\n"
        statement += "Withdrawals:\n"
        for w in self.withdrawals:
            statement += f"  -{w}\n"
        statement += f"Loan balance: {self.loans}"
        return statement
    def change_owner(self, new_name):
        old_name = self.name
        self.name = new_name
        return f"Account owner changed from {old_name} to {self.name}"
    def apply_interest(self):
        if self.is_closed:
            return "Account is closed."
        if self.get_balance()<=0:
            return "No interest added on zero or negative balance"
        interest = self.get_balance() * 5 / 100
        self.deposits.append(interest)
        return f"{self.name}, 5% interest of {interest} added. New balance: {self.get_balance()}"
    def view_account_details(self):
        return f"Owner: {self.name}\nBalance: {self.get_balance()}\nLoan: {self.loans}\nFrozen: {self.is_frozen}\nClosed: {self.is_closed}"
    def freeze_account(self):
        if self.is_frozen:
            return "Account is already frozen."
        if self.get_balance() > 0:
            self.is_frozen = True
            return "Account has been frozen."
        else:
            return "Cannot freeze an empty account."
    def unfreeze_account(self):
        if not self.is_frozen:
            return "Account is already active."
        self.is_frozen = False
        return "Account has been unfrozen."
    def set_minimum_balance(self, amount):
        if amount >= 0:
            self.min_balance = amount
            return f"Minimum balance set to {amount}"
        else:
            return "Minimum must be zero or more."
    def close_account(self):
        if self.is_closed:
            return "Account is already closed."
        if self.get_balance() == 0 and self.loans == 0:
            self.deposits = []
            self.withdrawals = []
            self.is_closed = True
            return "Account successfully closed."
        else:
            return "Cannot close account. Balance or loan must be zero."

acc1 = Account("Meron")
acc2 = Account("Kidane")

print(acc1.deposit(500))
print(acc1.withdraw(200))
print(acc1.transfer(100, acc2))
print(acc1.get_loan(300))
print(acc1.repay_loan(100))
print(acc1.freeze_account())
print(acc1.apply_interest())

