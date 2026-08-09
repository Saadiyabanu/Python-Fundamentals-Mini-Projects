def deposit(amount,acc_no,bank_accounts):
    if(amount<=0 ):
        print("Amount to be deposited should be greater than zero.")
    else:
        bank_accounts[acc_no]["balance"]=bank_accounts[acc_no]["balance"]+amount
        print("Amount Deposited Successfully")
        print("Current balance:",bank_accounts[acc_no]["balance"])
def withdraw(with_amount,acc_no,bank_accounts):
    if(with_amount<=0 ):
        print("Amount to be withdraw should be greater than zero.")
    elif(bank_accounts[acc_no]["balance"]-with_amount<0 ):
        print("Insuffcient balance.")
    else:
        bank_accounts[acc_no]["balance"]=bank_accounts[acc_no]["balance"]-with_amount
        print("Amount Withdraw Successfully")
        print("Current balance:",bank_accounts[acc_no]["balance"])
def check_balance(acc_no, bank_accounts):
    print("Current balance:",bank_accounts[acc_no]["balance"])

bank_accounts={
    1001:{
        "name":"abc",
        "balance":5000 },
    1002:{
        "name":"efg",
        "balance":5000
    },
    1003:{
        "name":"xyz",
        "balance":5000
    },
    1004:{
        "name":"pqr",
        "balance":5000
    },
    1005:{
        "name":"lmn",
        "balance":5000
    }
}
while True:
    print("-------------MENU-------------")
    print("1. Enter 1 to Deposit money")
    print("2. Enter 2 to Withdraw money")
    print("3. Enter 3 to check balance")
    print("4. Enter 4 to Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        acc_no=int(input("Enter your account no: "))
        if(acc_no in bank_accounts):
            amount = float(input("Enter amount to deposit: "))
            deposit(amount,acc_no,bank_accounts)
        else:
           print("Account not found")

    elif choice == "2":
        acc_no=int(input("Enter your account no: "))
        if(acc_no in bank_accounts):
            with_amount = float(input("Enter amount to withdraw: "))
            withdraw(with_amount,acc_no,bank_accounts)
        else:
           print("Account not found")

    elif choice == "3":
        acc_no=int(input("Enter your account no: "))
        if(acc_no in bank_accounts):
            check_balance(acc_no, bank_accounts)
        else:
           print("Account not found")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
   