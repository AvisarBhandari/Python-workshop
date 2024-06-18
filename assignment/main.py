# Assignment 1: Number Comparison
# : Write a program that takes two numbers as input and prints which one is larger, or if they are equal.
# :Prompt the user to enter two numbers.Use an if statement to compare the numbers.Print the appropriate message.

def number_comparison():
    while True:
        a = int(input("Enter the first Number"))
        b = int(input("Enter the secound Number"))
        if a>b:
            return a
            break
        if b>a:
            return b
            break

# Assignment 2: Odd or Even
# : Write a program that determines if a given number is odd or even.
# :Prompt the user to enter a number.Use an if statement to determine if the number is odd or even.Print the appropriate message.

def Odd_Or_Even():
    x = int(input("Enter a Number: "))
    if (x%2 ==0):
        return f"{x} is even"
    else:
        return f"{x} is odd"



# Assignment 3: Grade Classification
# : Write a program that classifies a student's grade based on their score.
# :Prompt the user to enter a score between 0 and 100.Use if statements to classify the score into grades (A, B, C, D, F).Print the appropriate grade.
# :

#     A: 90-100
#     B: 80-89
#     C: 70-79
#     D: 60-69
#     F: 0-59
def Grade_Classification():
    grade = int(input("Enter the score between 0 - 100: "))
    
    if grade >= 0 and grade <= 100:
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"
    else:
        return "Invalid score!!"
    

#     Assignment 4: Leap Year Checker
# : Write a program to check if a given year is a leap year.
# :Prompt the user to enter a year.Use nested if statements to check the leap year conditions.Print whether the year is a leap year or not.
# :

#     A year is a leap year if it is divisible by 4.
#     However, if the year is also divisible by 100, it is not a leap year unless it is also divisible by 400.

def Leap_Year_Checker():
    year = int(input("Enter a year: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f"{year} is a leap year."
            else:
                return f"{year} is not a leap year."
        else:
            return f"{year} is not a leap year."
    else:
        return f"{year} is not a leap year."



# BMI Calculator
# : Write a program that calculates the Body Mass Index (BMI) and categorizes it.
# :Prompt the user to enter their weight (in kilograms) and height (in meters).Calculate the BMI using the formula: BMI = weight / (height ** 2).Use if statements to categorize the BMI into underweight, normal weight, overweight, or obesity.Print the BMI value and its category.


#     Underweight: BMI < 18.5
#     Normal weight: 18.5 <= BMI < 24.9
#     Overweight: 25 <= BMI < 29.9
#     Obesity: BMI >= 30

def BMI_Calculator():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "UnderWeight"
    elif bmi < 24.9:
        category = "Normal Weight"
    elif bmi < 29.9:
        category = "OverWeight"
    else:
        category = "Obesity"
    return f"Your BMI is : {bmi:.2f} \n5Your BMI category is: {category}"
    



if __name__ == "__main__":
    print("\tMenu:")
    print("1. Number Comparison")
    print("2. Odd or Even Check")
    print("3. Grade Classification")
    print("4. Leap Year Checker")
    print("5. BMI Calculator")
    choice = int(input("Enter your choice (1-5): "))
    menu = {
        1: number_comparison,
        2: Odd_Or_Even,
        3: Grade_Classification,
        4: Leap_Year_Checker,
        5: BMI_Calculator
    }
    
    selected_function = menu.get(choice)
    
    if selected_function:
        print(selected_function())
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")