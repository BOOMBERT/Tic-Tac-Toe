from typing import List
import check_the_board


class GameBoard:
    def __init__(self) -> None:
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.free_fields = [str(i) + str(j) for i in range(3) for j in range(3)]

    def __str__(self) -> str:
        return f"{'-' * 9}\n".join((" | ".join(i) + "\n" for i in self.board)) +\
            f"\nFree fields -> {', '.join(self.free_fields)}"

    def set_the_mark(self, x_position: str, y_position: str, mark: str) -> bool:
        position_of_fields = {"0", "1", "2"}
        if x_position in position_of_fields and y_position in position_of_fields:
            x_position, y_position = int(x_position), int(y_position)

        else:
            print("Wrong data! Re-enter the correct data.\n")
            return False

        if self.board[int(x_position)][int(y_position)] != " ":
            print("This field is taken. Try again!\n")
            return False

        self.board[int(x_position)][int(y_position)] = mark
        self.update_free_fields(x_position, y_position)

        return True

    def update_free_fields(self, x_position: int, y_position: int) -> None:
        try:
            self.free_fields.remove(str(x_position) + str(y_position))
        except ValueError:
            print("The free fields are not synchronized with the board.")


def whose_turn(free_places: List[str]) -> str:
    return "O" if len(free_places) % 2 != 0 else "X"


def whoever_won(board: List[List[str]], mark: str) -> bool:
    board_lines = "".join("".join(line) for line in board)

    if check_the_board.check_horizontal_lines(board_lines) or \
            check_the_board.check_vertical_lines(board_lines) or \
            check_the_board.check_diagonal_lines(board_lines):
        print(f"Player with '{mark}' won\n")
        return True

    if check_the_board.is_draw(board_lines):
        print("Draw\n")
        return True

    return False


def game() -> None:

    print("Welcome to the tic-tac-toe game. Good luck!\n")
    game_board = GameBoard()

    while True:
        current_turn = whose_turn(game_board.free_fields)

        while True:
            print(game_board)
            print(f"Now the player with '{current_turn}' chooses the field\n")

            x_position = input("Enter the horizontal position (0, 1 or 2) -> ")
            y_position = input("Enter the vertical position (0, 1 or 2) -> ")
            print()

            if game_board.set_the_mark(x_position, y_position, current_turn):
                break

        if whoever_won(game_board.board, current_turn):
            print(game_board)

            play_again = input(
                "\nIf you want to play again, type 'y' or "
                "if you want to quit the game, type any character -> "
            )

            if play_again.lower() == "y":
                print("\nNew board!\n")
                game_board = GameBoard()

            else:
                print("Successful exit!")
                break


if __name__ == "__main__":
    game()
