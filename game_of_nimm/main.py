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
    stones = 20  # Initialize the game with 20 stones
    player = 1   # Player 1 starts the game

    # Continue the game loop until all stones are taken
    while stones > 0:
        print(f"There are {stones} stones left.")

        # Prompt current player to choose how many stones to remove (1 or 2)
        remove_stones = int(input(f"Player {player} would you like to remove 1 or 2 stones? "))

        # Validate the player's input: must be 1 or 2
        while remove_stones not in [1, 2] or remove_stones > stones:
            remove_stones = int(input("Please enter 1 or 2: "))
        
        stones -= remove_stones    # Update the number of stones left
        print()

        # Check if the game is over (no stones left)
        if stones == 0:
            # The player who took the last stone loses, so the other player wins
            if player == 1:
                winner = 2
            else:
                winner = 1
            print(f"Player {winner} wins!")
        else:
            # Switch turns between player 1 and player 2
            if player == 1:
                player = 2
            else: player = 1

# necessary boilerplate to start execution
if __name__ == '__main__':
    main()