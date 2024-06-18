sub1 = float(input("Mark of 1st subject: "))
sub2 = float(input("Mark of 2nd subject: "))
sub3 = float(input("Mark of 3rd subject: "))
sub4 = float(input("Mark of 4th subject: "))
sub5 = float(input("Mark of 5th subject: "))

if (sub1 > 100 or sub2 > 100 or sub3 > 100 or sub4 > 100 or sub5 > 100):
    print("Invalid Number!")
else:
    total = sub1 + sub2 + sub3 + sub4 + sub5
    gpa = (total * 4) / 500
    print("GPA =", gpa)
    if gpa >= 3.6 and gpa <=4:
        print("A")
    elif gpa >=2.6 and gpa <3.6:
        print("B")
    elif gpa >=2.0 and gpa <=2.5:
        print("C")
    elif gpa >= 1.6:
        print("D")
    else:
        print("F")