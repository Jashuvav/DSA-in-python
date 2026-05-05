class ATM:
   def __init__(self, balance=0):
      self.balance = balance
   def check_balance(self):
      print("Available balance: ", self.balance)
   def deposit(self, amount):
      self.balance += amount
      print("Deposit:", amount)
   def withdraw(self, amount):
      if amount > self.balance:
         print("Insufficient funds")
      else:
         self.balance -= amount
         print("Withdraw:", amount)
atm = ATM(1000)
while True:
   print("\n1. Check Balance")
   print("2. Deposit")
   print("3. Withdraw")
   print("4. Exit")
   choice = input("Enter your choice: ")
   if choice == '1':
      atm.check_balance()
   elif choice == '2':
      amount = float(input("Enter amount to deposit: "))
      atm.deposit(amount)
   elif choice == '3':
      amount = float(input("Enter amount to withdraw: "))
      atm.withdraw(amount)
   elif choice == '4':
      print("Thank you for using the ATM.")
      break
   else:
      print("Invalid choice. Please try again.")