class Account:
   
    
      def __str__(self, number, pin, owner):
        self.number = number
        self.__pin = pin
        self.__owner = owner
        self.__balance = 500
        # self.cash=cash
        self.__overdraft_limit = 0
        self.__interest_rate = 300
        self.__frozen = False
        self.__transaction_history = []
        self.__min_balance = 0
        # self.__amount= amount

      def show_balance(self,pin):
        if self.__pin == pin:
            return self.__balance
        else:
            return "Wrong PIN"

      def view_account_details(self):
        return f"Account Owner: {self.__owner}\nAccount Number: {self.number}\nCurrent Balance: {self.__balance}"

      def change_account_owner(self, new_owner):
        self.__owner = new_owner
        
#       def add_cash(self,cash):
#               return self.__balance+cash
                
              
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

accounts= Account(number=1234,pin=3232,owner="jane wango")
print(accounts)
print(accounts.show_balance(pin=3232))
print(accounts.view_account_details())
print(accounts.change_account_owner("Esther Nyokabi"))
# print(accounts.add_cash(cash=3000))
print(accounts.account_statement())
print(accounts.set_overdraft_limit(500))
print(accounts.calculate_interest())
print(accounts.freeze_account())
print(accounts.unfreeze_account())
print(accounts.transaction_history())
# print(accounts.set_min_balance())
print(accounts.transfer_funds(recipient="john",amount=50))

