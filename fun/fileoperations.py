import os

cont ='y'

f = open("sample.txt", "w")

while (cont=="y" or cont=="Y"):

    cont = input("Please enter y to continue.\n")

    select = int(input("1. Create a new file\n"
                       "2. Add value to an existing file\n"
                       "3. Copy data from one file to another\n"
                       "4. Rewrite the file with new content\n"))

    if (select == 1):
        content = input("Enter value to be entered in a file\n")
        f.write(f"\n{content}\n")
        f.close()
        f = open("sample.txt", "r")
        print("The content of the file is as follows\n")
        print(f.read())
        f.close()
    elif (select == 2):
        f = open("sample.txt", "a")
        content = input("Enter content to append to a file\n")
        f.write(f"\n{content}\n")
        f.close()
        f = open("sample.txt", "r")
        print("The content of the file is as follows\n")
        print(f.read())
        f.close()
    elif (select == 3):
        f = open("sample.txt", "r")
        lines = f.readlines()
        f.close()
        print(f"Lines: {lines}")
        f = open("sample2.txt", "a")
        for l in lines:
            f.write(l)
        f.close()
        f = open("sample2.txt", "r")
        print("The content of the sample2 file is as follows\n")
        print(f.read())
        f.close()
    else:
        f = open("sample.txt", "w")
        content = input("Enter the new override content\n")
        f.write(f"\n{content}\n")
        f.close()
        f = open("sample.txt", "r")
        print("The content of the sample2 file is as follows\n")
        print(f.read())
        f.close()
