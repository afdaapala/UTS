class Account:
    def __init__(self, type):
        self.type = type
        self.balance = float(input(f"Enter initial balance for {self.type}: "))
    def read_balance(self):
        return self.balance
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

class Customer:
    def __init__(self):
        self.savings = Account("Savings")
        self.loan = Account("Loan")
    def read_amount(self):
        return float(input("Enter amount: "))
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

class Bank:
    def __init__(self):
        self.customer = Customer()
    def main(self):
        print("\n########## Start Banking! ##########\n")
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Display")
            print("4. Transfer")
            print("5. Exit\n")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("########### Deposit Menu ###########\n")
                amount = float(input("Enter the amount to deposit: "))
                self.customer.savings.deposit(amount)
            elif choice == 2:
                print("########### Withdraw Menu ###########\n")
                amount = float(input("Enter the amount to withdraw: "))
                self.customer.savings.withdraw(amount)
            elif choice == 3:
                print("########### Display Menu ###########\n")
                self.customer.show_status()
            elif choice == 4:
                print("########### Transfer Menu ###########\n")
                self.customer.transfer()
            elif choice == 5:
                break
            else:
                print("\nInvalid choice!\nPlease enter a valid choice! (1/2/3/4/5):")

if __name__ == "__main__":
    main = Bank()
    main.main()
    print("\nThank you for banking with us!\n")
    print("########## End Banking! ##########\n")