class Client:
    def __init__(self,cin,firstName,lastName,tel=""):
        #private attributes
        self.__cin=cin
        self.__firstName=firstName
        self.__lastName=lastName
        self.__tel=tel
        #list to store all accounts of client   
        self.accounts=[]
#add new account to client
    def addAccount(self,account):
        self.accounts.append(account)
#display client informations        
    def display(self):
        print(self.__cin,self.__firstName,self.__lastName,self.__tel)

    def listAccounts(self):
        print("Client accounts:")
        for i in self.accounts:
            print("Account",i.code,"Balance:",i.balance)
class Account:
    #static variable to count total accounts    
    nbAccounts=0  

    def __init__(self,owner):
        self.owner=owner
        self.balance=0
        Account.nbAccounts+=1
        self.code=Account.nbAccounts
        self.transactions=[]

        owner.addAccount(self)
#add money to the account   
    def credit(self,amount):
        if amount<=0:
            print("Invalid amount")
            return
        self.balance+=amount
        self.transactions.append("Credit: +" + str(amount))

    def debit(self,amount):
        if amount<=0:
            print("Invalid amount")
            return
        if amount>self.balance:
            print("Insufficient balance")
            return
        self.balance-=amount
        self.transactions.append("Debit: -" + str(amount))
#transfer money to another account
    def transfer(self,amount,account):
        if amount>self.balance:
            print("Transfer not allowed")
            return
        self.debit(amount)
        account.credit(amount)
        self.transactions.append("Transfer to account " + str(account.code))

    def displayTransactions(self):
        for j in self.transactions:
            print(j)

    def display(self):
        print("Account:",self.code,"Balance:",self.balance)
#display total number of accounts
    @staticmethod
    def displayNbAccounts():
        print("Total accounts:",Account.nbAccounts)
