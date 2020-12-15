cont ="y"

password = ""

if password == "":
    password = input("Create your password.")

def check_sufficient_funds_and_deduct(amt, price):
    amt -= price
    if (amt < 0):
        print(f"You have insufficient funds to make a purchase.")
        amt += price
    return amt

class Product:

    def __init__(self, price=0):
        self.price = price

    def price(self):
        return self.price

class Soda(Product):

    def __init__(self, price=0):
        self.price = 20

class Chips(Product):

    def __init__(self, price=0):
        self.price = 15


class Lays(Chips):

    def __init__(self, price=0):
        self.price = 30

class Coke(Soda):

    def __init__(self, price=0):
        self.price = 35

class Pepsi(Soda):

    def __init__(self, price=0):
        self.price = 30

class Water(Product):

    def __init__(self, price=0):
        self.price = 10

amount = int(input("Insert amount:\n"))
print(f"You have Rs. {amount} in account.")


counter = 0

while (counter <= 3):
    reenter_password = input("Enter password:\n")
    if password != reenter_password and counter == 3:
       print("Your account is locked.")
       break
    elif password != reenter_password:
        print(f"Your have {3- counter} attempt(s) left.")
        counter += 1
    else:
        break


while (password == reenter_password) and (cont=='y' or cont =='Y'):

    while (amount < 10):
        print(f"You have insufficient funds to make a purchase.")
        recharge = int(input("Recharge amount:\n"))
        amount += recharge


    soda = Soda()
    lays = Lays()
    water = Water()
    pepsi = Pepsi()
    coke = Coke()
    chips = Chips()


    select = int(input("Please select from the following\n"
                       f"1. Soda - Rs. {soda.price} \n2. Lays - Rs. {lays.price} \n3. Water - Rs. {water.price} \n"
                       f"4. Pepsi - Rs {pepsi.price} \n5. Coke - Rs {coke.price}\n6. Chips - Rs {chips.price}\n"))

    if (select == 1):
        amount = check_sufficient_funds_and_deduct(amount, soda.price)
    elif (select == 2):
        amount = check_sufficient_funds_and_deduct(amount, lays.price)
    elif (select == 3):
        amount = check_sufficient_funds_and_deduct(amount, water.price)
    elif (select == 4):
        amount = check_sufficient_funds_and_deduct(amount, pepsi.price)
    elif (select == 5):
        amount = check_sufficient_funds_and_deduct(amount, coke.price)
    else:
        amount = check_sufficient_funds_and_deduct(amount, chips.price)
    print(f"You have Rs. {amount} left.")

    cont = input("Please enter 'y' if you wish to continue:\n")