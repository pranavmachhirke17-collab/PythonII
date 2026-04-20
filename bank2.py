class bank_account:
    def __init__(self,account_number,balance,check_balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
    
    def check_balance(self):
        print(f"Current balance is {self.balance}.")    

account_no = input("Enter your account number: ")
initial_balance = float(input("Enter initial balance: "))

while True:
    user_account = bank_account(account_no, initial_balance,True)
    print("Choose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        user_account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        user_account.withdraw(amount)
    elif choice == '3':
        user_account.check_balance()
        break
    else:
        print("Invalid choice. Please try again.")