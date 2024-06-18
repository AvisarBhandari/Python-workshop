import random

def main():
    player1 = input("Enter Name of player 1? \n-> ")
    player2 = input("Enter Name of player 2? \n-> ")
    position_player_one = 0
    position_player_two = 0
    
    while True:
        position_player_one = game(player1, position_player_one)
        if position_player_one >= 24:
            print(f"{player1} Won!!")
            break
        
        position_player_two = game(player2, position_player_two)
        if position_player_two >= 24:
            print(f"{player2} Won!!")
            break

def game(player_name,position):
    special_positions = {24: 1, 14: 3, 19: 7, 17: 9}
    
    
    input(f"{player_name}, press Enter to Roll")
    roll = random.randint(1, 6)
    print(f"{player_name} rolled a {roll}")
    position += roll

    if position in special_positions:
        new_position = special_positions[position]
        print(f"{player_name} landed on {position}, so Moving back to {new_position}.")
        position = new_position

    print(f"{player_name}'s current position is {position}")
    return(position)
    
    


if __name__ == "__main__":
    main()