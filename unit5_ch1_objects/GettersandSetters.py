#Define class BankAccount
class BankAccount:
    #Initialize balance to 0
    def __init__(self, name, balance = 0.0):
        self.log("Account created!")
        self.name = name
        self.balance = balance

    def getBalance(self): #Getter for balance
        self.log("Balance checked at " + str(self.balance))
        return self.balance

    def setBalance(self, newBalance): #Setter for balance
        self.log("Balance changed to " + str(newBalance))
        self.balance = newBalance

    def log(self, message): #Logging method
        myLog = open("Log.txt", "a")
        print(message, file = myLog)
        myLog.close()

myBankAccount = BankAccount("David Joyner")
myBankAccount.setBalance(20.0)
print(myBankAccount.getBalance())


