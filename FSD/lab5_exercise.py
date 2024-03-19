class Bank:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            print("\nInsufficient balance!!!\n")
            return self.balance
        self.balance -= amount
        print("\nSuccessfully withdrawn! amount: ", amount)
        return self.balance
    def display(self):
        return self.balance
    def read(self):
        return self.balance
    def main(self):
        print("\n########## Start Banking! ##########\n")
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Display")
            print("4. Exit\n")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("########### Deposit Menu ###########\n")
                amount = int(input("Enter the amount to deposit: "))
                print("Successfully deposited! amount: ", amount)
                print("Current balance: ", self.deposit(amount))
            elif choice == 2:
                print("########### Withdraw Menu ###########\n")
                amount = int(input("Enter the amount to withdraw: "))
                print("Current balance: ", self.withdraw(amount))
            elif choice == 3:
                print("########### Display Menu ###########\n")
                print("Current balance: ", self.display())
            elif choice == 4:
                break
            else:
                print("\nInvalid choice!\nPlease enter a valid choice!:")

if __name__ == "__main__":
    balance = int(input("Enter the initial balance: "))
    main = Bank(balance)
    main.main()
    print("\nThank you for banking with us!\n")
    print("########## End Banking! ##########\n")
