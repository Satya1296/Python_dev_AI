from bankAccount import BankAccount

def main():
    print("Bank: ",BankAccount.bank_name)
    acc1=BankAccount("Ravi kumar","Savings",5000,"1234")
    acc2=BankAccount("Anita Sharma","Current",20000,"5678")

    print(acc1)
    print(acc2)

    print("Total accounts:",BankAccount.get_total_accounts())
    acc1.deposit(2000)
    print("Deposit 2000 -> ", acc1.balance)
    acc1.withdraw(1500,"1234")
    print("Withdraw 1500 -> ",acc1.balance)

    interest=acc1.add_annual_interest()
    print("Interest added:", interest)
    print("Balance now:", acc1.balance)

    acc1.change_pin("1234", "4321")
    print("PIN changed successfully")   

    try:
        acc1.withdraw(500,"1111")
    except ValueError as e:
        print("Blocked (wrong PIN):",e)

    try:
        acc1.withdraw(6000,"4321")
    except ValueError as e:
        print("Blocked(below min):",e)

    try:
        acc1.deposit(-100)
    except ValueError as e:
        print("Blocked (negative):", e)

    try:
        acc1.balance=99999
    except AttributeError as e:
        print("Blocked (write balance):", e)

if __name__ == "__main__":
    main()