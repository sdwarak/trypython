month = int(input("Enter month of the year:\n"))

if 3 <= month <= 5:
    print("It's summer.")
elif 6 <= month <= 8:
    print("It's mansoon.")
elif 9 <= month <= 11:
    print("It's autumn.")
else:
    print("It's winter.")