class BalanceException(Exception):
  pass

class BankAccont:
  def __init__(self, initialAmount, accName):
    self.balance = initialAmount
    self.name = accName
    print(f"\nAccont '{self.name}' creates. \nBalance = ${self.balance:.2f}")
    
  def getBalance(self):
    print(f"\nAccount '{self.name}' balance = $ {self.balance:.2f}")
  
  def deposit(self, amount):
    self.balance = self.balance + amount 
    print("\nDeposit complete. ")
    self.getBalance()

  def viableTransaction(self, amount):
    if self.balance >= amount:
      return
    else:
      raise BalanceException(
        f"\n Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
      
  def withdraw(self, amount):
    try:
      self.viableTransaction(amount)
      self.balance = self.balance - amount
      print("\nWithdraw Complete.")
      self.getBalance()
    except BalanceException as error:
      print(f'\n Withdaw interrupted: {error}')
  
  