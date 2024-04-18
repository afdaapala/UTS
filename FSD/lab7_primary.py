import datetime
import random as rand

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Account:
    def __init__(self, type):
        self.type = type
        # self.balance = float(input(f"Enter initial balance for {self.type}: "))
        self.balance = float(rand.randint(100, 2000))
        # print(f"Initial balance for {self.type} account: ${self.balance}")
    def read_balance(self):
        return self.balance
    def match_fieldtype(self, field):
        if field == "balance":
            return self.balance
        else:
            return None
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"Deposited ${amount} to {self.type} account.")
            print(f"{self.type} account current balance: ${self.balance}")
        else:
            print("Invalid input: Please enter a non-negative amount.")
            print(f"{self.type} account current balance: ${self.balance}")
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
            print(f"{self.type} account current balance: ${self.balance}")
            return
        else:
            self.balance -= amount
            print(f"Withdrawn ${amount} from {self.type} account.")
            print(f"Current balance: ${self.balance}")
    def show_balance(self):
        print(f"{self.type} account balance: ${self.balance}")
    def transfer(self, amount, target_account):
        self.balance -= amount
        target_account.deposit(amount)
        print(f"Transferred ${amount} from {self.type} account to {target_account.type} account.")
    def account_information(self):
        print(f"{self.type} account balance: ${self.balance}")

class Customer:
    def __init__(self):
        self.name = input("Enter Customer name: ")
        self.savings = Account("Savings")
        self.loan = Account("Loan")
    def read_amount(self):
        return float(input("Enter amount: "))
    def verify_customer(self):
        pass
    def lookupAccount(self, account):
        if account == "savings":
            return self.savings
        elif account == "loan":
            return self.loan
        else:
            return None
    def withdraw(self):
        amount = self.read_amount()
        self.savings.withdraw(amount)
    def show_status(self):
        print("Customer accounts:")
        self.savings.show_balance()
        self.loan.show_balance()
    def transfer(self):
        amount = self.read_amount()
        self.savings.transfer(amount, self.loan)
    def transfer_to(self, target_account):
        amount = self.read_amount()
        self.savings.transfer(amount, self.name.lookupAccount(target_account))
    def deposit(self):
        amount = self.read_amount()
        self.savings.deposit(amount)
        

class Bank:
    def __init__(self):
        self.customers = []    
    def view_customer(self):
        print("\n########### List of Customers ###########\n")
        for customer in self.customers:
            print(f"{self.customers.index(customer)+1}. {customer.name}")
        print("\n")
    def add_customer(self):
        self.customers.append(Customer())
    def customer_menu(self):
        for customer in self.customers:
            print(f"{self.customers.index(customer)+1}. {customer.name}")
        customer_choice = int(input("Select number of the customer to Login: "))
        return customer_choice
    def main(self):
        print("\n########## Start Banking! ##########\n")
        while True:
            print("1. Login")
            print("2. View list of customers")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("########### Customer Menu ###########\n")
                customer_choice = self.customer_menu()
                while True:
                    print(f"\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Display")
                    print("4. Transfer")
                    print("5. Exit\n")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        print("########### Deposit Menu ###########\n")
                        self.customers[customer_choice].deposit()
                    elif choice == 2:
                        print("########### Withdraw Menu ###########\n")
                        self.customers[customer_choice].withdraw()
                    elif choice == 3:
                        print("########### Display Menu ###########\n")
                        self.customers[customer_choice].show_status()
                    elif choice == 4:
                        print("########### Transfer Menu ###########\n")
                        self.customers[customer_choice].transfer()
                    elif choice == 5:
                        break
                    else:
                        print("\nInvalid choice!\nPlease enter a valid choice! (1/2/3/4/5):")
            elif choice == 2:
                self.view_customer()
            elif choice == 3:
                break
            else:
                print("\nInvalid choice!\nPlease enter a valid choice! (1/2/3):")

if __name__ == "__main__":
    main = Bank()
    number_of_customers = input("Enter the number of customers: ")
    if number_of_customers.isdigit():
        number_of_customers = int(number_of_customers)
    else:
        print("Invalid input: Please enter a number.")
        number_of_customers = int(input("Enter the number of customers: "))
        
    for customer in range(number_of_customers):
        print(f"Customer {customer+1}")
        main.add_customer()
        main.customers[customer].show_status()
    main.main()
    print("\nThank you for banking with us!\n")
    print("########## End Banking! ##########\n")