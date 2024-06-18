import random

a = random.randint(1, 3)

b = int(input("Enter a number - (1 for scissors) - (2 for paper) - (3 for rock): "))

print(f"Python chose: {a}")

if a == b:
    print("Draw")
elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print("Python won")
elif (b == 1 and a == 2) or (b == 2 and a == 3) or (b == 3 and a == 1):
    print("You won ")
else:
    print("Invalid input")