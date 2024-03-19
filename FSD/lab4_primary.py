class Bank():
    def __init__(self, username, account, balance):
        self.username = username
        self.account = account 
        self.balance = balance
    def depositBalance(self, amount):
        self.balance += amount
        print(f"Succesfully deposited {amount} to your account")
    def withdrawBalance(self, amount):
        amount = input("Please enter the amount you want to withdraw : ")
        self.balance -= amount
        print(f"Succesfully withdraw {amount} from your account")
    def showBalance(self, balance):
        print(self.balance)
        print(f"You have {balance} on your account")

main = Bank("Amar", 1, 1000)        
opt = input("choose options 1/2/3/4 : ")
        
def bankMenu(opt):
    if opt == "1":
        main.depositBalance()
    elif opt == "2":
        main.withdrawBalance()
    elif opt == "3":
        main.showBalance()
    elif opt == "4":
        print("exiting the app")
        exit


bankMenu(opt)

