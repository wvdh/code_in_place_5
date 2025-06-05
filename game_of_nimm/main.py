"""
This is "The ancient Game of Nimm" and goes as follows:
The game starts with a pile of 20 stones between the players.
The two players alternate turns. On a given turn,
a player may take either 1 or 2 stone from the center pile.
The two players continue until the center pile has run out of stones.
The last player to take a stone loses. 
"""

import random

def main():
    """
    You should write your code here. 
    """
    stones = 20  # Start with 20 stones
    player = 1   # Track the player (1 or 2)

    print("The Ancient Game of Nimm")
    print()

    while stones > 0:
        print(f"There are {stones} stones left.")
        remove_stones = int(input(f"Player {player} would you like to remove 1 or 2 stones? "))

        while remove_stones not in [1, 2] or remove_stones > stones:
            remove_stones = int(input("Please enter 1 or 2: "))
        
        stones -= remove_stones
        print()

        if stones == 0:
            if player == 1:
                winner = 2
            else:
                winner = 1
            print(f"Player {winner} wins!")
        else:
            if player == 1:
                player = 2
            else: player = 1

if __name__ == '__main__':
    main()