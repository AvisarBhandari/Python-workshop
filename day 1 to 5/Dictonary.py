name = input("Enter your name: ")
age = input("Enter your age: ")
nation = input("Enter your nationality: ")

student = {"Name": name,"Age": age,"Nationality": nation
}

print('Items:',student.items())

print("User Information:")
for key, value in student.items():
    print(f"{key}: {value}")

