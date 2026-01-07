# Advanced Smart Bank System using Multilevel Inheritance

class Bank:
    bank_name = "SBI"
    branch = "Punjagutta"

    def bank_info(self):
        return f"Bank: {Bank.bank_name}, Branch: {Bank.branch}"


class Account(Bank):
    def __init__(self, acno, balance):
        self.acno = acno
        self.balance = balance

    def account_info(self):
        return f"Account No: {self.acno}, Balance: ₹{self.balance}"


class Customer(Account):
    def __init__(self, cname, acno, balance):
        self.cname = cname
        super().__init__(acno, balance)

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ₹{amount}. New Balance: ₹{self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn ₹{amount}. New Balance: ₹{self.balance}"
        else:
            return "Insufficient Balance"


# Demo
c1 = Customer("Rahul", 123456789, 5000)
print(c1.bank_info())
print(c1.account_info())
print(c1.deposit(2000))
print(c1.withdraw(3000))
