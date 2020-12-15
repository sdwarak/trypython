for i in range(0,51):
    if (i % 5) == 0 and (i % 3) == 0:
        print(f"{i} FizzBuzz")
    elif (i % 5) == 0:
        print(f"{i} Buzz")
    elif (i % 3) == 0:
        print(f"{i} Fizz")
    else:
        print(f"{i}")
