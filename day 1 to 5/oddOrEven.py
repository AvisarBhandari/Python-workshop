x = float(input("Enter a Number: "))
if x.is_integer():
    if (x % 2 == 0):
        print("Even")
    else:
        print("Odd")
else:
    print("Invalid")
