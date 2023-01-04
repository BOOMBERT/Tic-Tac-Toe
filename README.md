
# Tic-Tac-Toe

Tic-Tac-Toe game to play in the terminal for 2 players.


## Controls

- Player with 'O' always starts the game
- First you select the horizontal line and then the vertical line
- When you selecting a horizontal line, you can choose lines 0, 1 or 2. Line 0 is at the top and line 2 is at the bottom
- When you selecting a vertical line, you can choose lines 0, 1 or 2. Line 0 is the first column and line 2 is the last column
- The game is looped, so it only ends when you enter a random character into the terminal at the end of the game




## Example excerpt from the terminal

```
  |   |  
---------
  |   |  
---------
  |   |  

Free fields -> 00, 01, 02, 10, 11, 12, 20, 21, 22
Now the player with 'O' chooses the field

Enter the horizontal position (0, 1 or 2) -> 1
Enter the vertical position (0, 1 or 2) -> 1

  |   |  
---------
  | O |  
---------
  |   |  

Free fields -> 00, 01, 02, 10, 12, 20, 21, 22
Now the player with 'X' chooses the field

Enter the horizontal position (0, 1 or 2) -> 2
Enter the vertical position (0, 1 or 2) -> 0

  |   |  
---------
  | O |  
---------
X |   |  

Free fields -> 00, 01, 02, 10, 12, 21, 22
Now the player with 'O' chooses the field

```


## Run Locally

Clone the project

```bash
  git clone https://github.com/BOOMBERT/Tic-Tac-Toe.git
```

Go to the project directory

```bash
  cd Tic-Tac-Toe
```

Start the program

```bash
  python main.py
```


## Authors

- [@BOOMBERT](https://github.com/BOOMBERT)


## License

[MIT](https://choosealicense.com/licenses/mit/)

