import random
p=0
while(True):
    input("Press enter to Roll")
    roll=random.randint(1,6)
    print(f"You rolled a {roll}")
    p+=roll
    if(p==24):
        print("You landed on 24,so Moving back to 1.")
        p=1
    elif(p==14):
        print("You landed in 14,so Moving back to 3.")
        p=3
    elif(p==19):
        print("You landed in 19,so Moving back to 7.")
        p=7
    elif(p==17):
        print("You landed in 17,so Moving back to 9.")

    print(f"Your current position is {p}")
    if p>24:
        print("You Won!!")
        break



