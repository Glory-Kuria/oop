class Account:
   
    
 def __init__(self, number, pin, owner, balance=0):
        self.number = number
        self.__pin = pin
        self.__owner = owner
        self.__balance = balance
        self.__overdraft_limit = 0
        self.__interest_rate = 0
        self.__frozen = False
        self.__transaction_history = []
        self.__min_balance = 0

def show_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Wrong PIN"

def view_account_details(self):
        return f"Account Owner: {self.__owner}\nAccount Number: {self.number}\nCurrent Balance: {self.__balance}"
def change_account_owner(self, new_owner):
        self.__owner = new_owner


def account_statement(self):
        return self.__transaction_history

def set_overdraft_limit(self, limit):
        self.__overdraft_limit = limit

def calculate_interest(self):
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        return f"Interest applied: {interest}"

def freeze_account(self):
        self.__frozen = True

def unfreeze_account(self):
        self.__frozen = False

def transaction_history(self):
        return self.__transaction_history

def set_min_balance(self, min_balance):
        self.__min_balance = min_balance

def transfer_funds(self, recipient, amount):
        if not self.__frozen and self.__balance >= amount:
            self.__balance -= amount
            recipient.__balance += amount
            self.__transaction_history.append(f"Transfer to {recipient.number}: ${amount}")
            recipient.__transaction_history.append(f"Transfer from {self.number}: ${amount}")
            return "Funds transferred successfully"
        else:
            return "Transfer failed"

def close_account(self):
        self.__owner = "Closed Account"
        self.__balance = 0
        self.__frozen = True
        self.__transaction_history = []
        return "Account successfully closed"