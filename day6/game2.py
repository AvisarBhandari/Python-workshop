import random
special_positions = {
    24: 1,
    14: 3,
    19: 7,
    17: 9}

p = 0
while True:
    input("Press enter to Roll")
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}")
    p += roll
        
    if p in special_positions:
        new_position = special_positions[p]
        print(f"You landed on {p}, so Moving back to {new_position}.")
        p = new_position
        
    print(f"Your current position is {p}")
        
    if p > 24:
        print("You Won!!")
        break