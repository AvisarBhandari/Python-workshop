# a = int(input("Enter first number: "))
# b = int(input("Enter secound number: "))
# choice=int( input("Enter 1 for add and 2 for sub "))
# if choice == 1:
#     print("Add=",a+b)
# elif choice == 2:
#     print("Sub=",a-b)
# else:
#     print("Invald operation")

# a = int(input("Enter first number: "))
# b = int(input("Enter secound number: "))
# choice=int( input("1 Add \n2 sub\n3 mul\n4 div\n5 average\nEnter Your Choice= "))

# if choice == 1:
#     print("Add=",a+b)
# elif choice == 2:
#     print("Sub=",a-b)
# elif choice ==3:
#     print("Mul=",a+b)
# elif choice == 4:
#     print("Div=",a/2)
# elif choice == 5:
#     print("Average=",(a+b)/2)
# else:
#     print("Invald operation")

# a = int(input("Enter first number: "))
# b = int(input("Enter secound number: "))
# choice=input("1 Add \n2 sub\n3 mul\n4 div\n5 average\nEnter Your Choice= ")


# if choice == ("Add" or "add"):
#     print("Add=",a+b)
# elif choice == ("sub" or "Sub"):
#     print("Sub=",a-b)
# elif choice == ("mul" or "Mul"):
#     print("Mul=",a+b)
# elif choice == ("Div" or "div"):
#     print("Div=",a/2)
# elif choice == ("Average" or "average"):
#     print("Average=",(a+b)/2)
# else:
#     print("Invald operation")

a = int(input("Enter first number: "))
b = int(input("Enter secound number: "))
choice=input("1 Add \n2 sub\n3 mul\n4 div\n5 average\nEnter Your Choice= ")
ch=choice.lower()

print(ch)

if ch == ("add"):
    print("Add=",a+b)
elif ch == ("sub"):
    print("Sub=",a-b)
elif ch == ("mul"):
    print("Mul=",a+b)
elif ch == ("div"):
    print("Div=",a/2)
elif ch == ("average"):
    print("Average=",(a+b)/2)
else:
    print("Invald operation")



