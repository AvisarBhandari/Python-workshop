import random

def main():
    num_players = int(input("Enter number of players: "))
    players = []
    positions = [0] * num_players
    
    for i in range(num_players):
        player_name = input(f"Enter Name of player {i + 1}? \n-> ")
        players.append(player_name)
    
    while True:
        for i in range(num_players):
            print("\n")
            positions[i] = game(players[i], positions[i])
            if positions[i] >= 24:
                print(f"{players[i]} Won!!")
                return

def game(player_name, position):
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
    return position
    
if __name__ == "__main__":
    main()
