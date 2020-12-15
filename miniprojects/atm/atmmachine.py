class BankAccount:
    def __init__(self, name, balance=0.00):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """make a deposit"""
        self.balance += amount
        print(f"Balance is Rs. {self.balance}")
        return self.balance

    def withdraw(self, amount):
        """make a withdrawal"""
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        print(f"Balance is Rs. {self.balance}")
        return self.balance

    def get_balance(self):
        """check the balance"""
        print(f"Balance is Rs. {self.balance}")
        return self.balance


def verify_pin(pin):
    if pin == '1234':
        return True
    else:
        return False

def log_in():
    tries = 0
    while tries < 4:
        pin = input('Please Enter Your 4 Digit Pin: ')
        if verify_pin(pin):
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin")
            tries += 1
    print("Too many incorrect tries. Could not log in.")
    return False

def main_menu():
    customer = BankAccount("Dwarak", 10000.0)

    select = int(input("Please select from the following\n"
                       "1. Check Balance \n2. Withdraw\n3. Deposit \n4. Show pin"))

    if (select == 1):
        customer.get_balance()
    elif (select == 2):
        amt = int(input("Enter amount to withdraw.\n"))
        customer.withdraw(amt)
    elif (select == 3):
        amt = int(input("Enter amount to deposit.\n"))
        customer.deposit(amt)
    else:
        print("1234")

def start_menu():
    print("Welcome to the atm!")
    if log_in():
        main_menu()
    print("Exiting Program")

start_menu()