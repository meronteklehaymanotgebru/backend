class Account:
    def __init__(self, name):
        self.name = name
        self.deposits = []
        self.withdrawals = []
        self.loans = 0
    def get_balance(self):
        total = 0
        for i in self.deposits:
            total += i
        summ = 0
        for j in self.withdrawals:
            summ += j
        balance = total - summ
        return balance
    def deposit(self, money):
        if money > 0:
            self.deposits.append(money)
            return f"{self.name}, your balance now is {self.get_balance()}"
        else:
            return "Deposit must be greater than zero."
    def withdraw(self, money):
        if money > 0:
            if self.get_balance() >= money:
                self.withdrawals.append(money)
                return f"{self.name}, you withdrew {money}. Remaining balance: {self.get_balance()}"
            else:
                return "You don't have enough money"
        else:
            return "Invalid amount"
    def show_balance(self):
        return f"{self.name}, your current balance is {self.get_balance()}"
    def transfer(self, amount, other_account):
        if amount <= 0:
            return "Transfer amount must be positive."
        if not isinstance(other_account, Account):
            return "Transfer failed. Recipient must be an Account object."
        if self.get_balance() >= amount and self.get_balance() > 100:
            self.withdrawals.append(amount)
            other_account.deposits.append(amount)
            return f"Transfer of {amount} to {other_account.name} successful. Your new balance is {self.get_balance()}"
        else:
            return "Transfer failed. Not enough balance or balance is below minimum limit."
    def get_loan(self, money):
        if self.loans < 500 and money > 0:
            self.deposits.append(money)
            self.loans += money
            return f"{self.name}, loan approved. New balance: {self.get_balance()}"
        else:
            return "Loan request denied."
    def repay_loan(self, money):
        if self.loans > 0:
            if money <= self.loans:
                self.loans -= money
                self.withdrawals.append(money)
                return f"{self.name}, you have {self.loans} loan left."
            else:
                extra = money - self.loans
                self.withdrawals.append(self.loans)
                self.loans = 0
                return f"{self.name}, loan fully repaid. Extra money: {extra}"
        else:
            return "No loan to repay."
    def get_statement(self):
        return f"{self.name}'s statement:\nDeposits: {self.deposits}\nWithdrawals: {self.withdrawals}\nLoan balance: {self.loans}"
    def get_loan_statement(self):
        return f"{self.name}, your loan balance is {self.loans}"
