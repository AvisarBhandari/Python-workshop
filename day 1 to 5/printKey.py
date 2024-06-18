student = {"name": "Avisar", "age": 21, "address": "Nepal"}
choice = input("Enter the key: ").lower()


if choice in student:
    print("The value is:", student[choice])
else:
    print("Invalid")
