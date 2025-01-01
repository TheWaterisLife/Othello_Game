# Othello Game

This is a Python implementation of the classic Othello (also known as Reversi) board game. It allows two players to play the game interactively through the terminal, with alternating moves between the two players (Black and White).

## Features
- **Board Setup**: The game starts with a standard 8x8 Othello board.
- **Legal Moves**: The game calculates valid moves for each player and allows them to choose where to place their pieces.
- **Tile Flipping**: After each move, the game flips the opponent's tiles when they are surrounded.
- **Turn Management**: The game alternates turns between the two players, Black (B) and White (W).
- **Game Over Conditions**: The game ends when neither player can make a move. The player with the most pieces on the board wins.

## How to Play
1. **Starting the Game**: The game starts with an initial board setup and asks the user to choose a starting board from a list of predefined configurations.
2. **Making a Move**: Players are prompted to enter their moves in the format `D8`, where the letter represents the column (A-H) and the number represents the row (1-8).
3. **Valid Moves**: The game will show available moves for the current player. If a player makes an invalid move, they will be prompted to try again.
4. **End of Game**: The game ends when no valid moves are available for either player, and the winner is announced based on the number of pieces on the board.

## Future Upgrades
In the future, I plan to upgrade this project to make it more **UI-friendly** with a graphical user interface (GUI). This will improve the user experience by making it easier to interact with the game, visualize the board, and play with different themes or modes.

## Requirements
- Python 3.x
- No external libraries are required for this version.

## How to Run
1. Clone or download this repository.
2. Navigate to the project directory in the terminal.
3. Run the Python file using the command:
