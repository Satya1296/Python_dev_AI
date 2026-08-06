class BankAccount:
    bank_name="State Bank of India"
    total_accounts=0
    interest_rate=4.0
    MIN_BALANCE=500
    _next_account_number=1001

    def __init__(self,holder_name,account_type,initial_deposit,pin):
        if initial_deposit < BankAccount.MIN_BALANCE:
            raise ValueError("Opening deposit below minimum balance")
        self.holder_name=holder_name
        self._account_number=BankAccount._next_account_number
        BankAccount._next_account_number+=1
        self._account_type=account_type
        self.__balance=initial_deposit
        self.__pin=pin
        BankAccount.total_accounts+=1

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Deposit must be positive")
        self.__balance+=amount
        return self.__balance

    def withdraw(self,amount,pin):
        self.verify_pin(pin)
        if amount<=0:
            raise ValueError("Withdrawal must be positive")
        if self.__balance-amount < BankAccount.MIN_BALANCE:
            raise ValueError(f"Insufficient funds.Minimum balance{BankAccount.MIN_BALANCE} must remain")
        self.__balance-=amount
        return self.__balance

    def verify_pin(self,pin):
        if pin!=self.__pin:
            raise ValueError("Incorrect PIN")

    def change_pin(self,old_pin,new_pin):
        self.verify_pin(old_pin)
        new_pin=str(new_pin)
        if(len(new_pin))!=4 or not new_pin.isdigit():
            raise ValueError("Pin must be exactly 4 digits")
        self.__pin=new_pin

    def add_annual_interest(self):
        interest=(self.__balance*BankAccount.interest_rate)/100
        self.__balance+=interest
        return interest

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @staticmethod
    def is_valid_amount(amount):
        return amount>0

    def __str__(self):
        return (f"Account number:{self._account_number}," f"Holder Name:{self.holder_name}, "f"Account type:{self._account_type}, "f"Balance:{self.__balance}")
    

    


