import sys


def get_board(board: list[list[str]]) -> str:
    return f"""
    {' | '.join(board[0])}
    ----------
    {' | '.join(board[1])}
    ----------
    { ' | '.join(board[2])}
    """


def set_board(board: list[list[str]], free_places: list[str],
              x_position: int, y_position: int, mark: str) -> None:

    if board[x_position][y_position] != ' ':
        print("\nThis place is taken. Try again!")

    else:
        board[x_position][y_position] = mark
        free_places.remove((str(x_position) + str(y_position)))


def display_free_places(free_places: list[str]) -> str:
    return "Empty places --> " + ", ".join(free_places)


def whose_turn(free_places: list[str]) -> str:
    return "O" if len(free_places) % 2 != 0 else "X"


def check_horizontal_lines(board: str) -> bool:
    return board[0:3] in ("OOO", "XXX") or \
           board[3:6] in ("OOO", "XXX") or \
           board[6:9] in ("OOO", "XXX")


def check_vertical_lines(board: str) -> bool:
    return board[0::3] in ("OOO", "XXX") or \
           board[1::3] in ("OOO", "XXX") or \
           board[2::3] in ("OOO", "XXX")


def check_diagonal_lines(board: str) -> bool:
    return board[0::4] in ('OOO', 'XXX') or \
           board[-3::-2][0:3] in ('OOO', 'XXX')


def is_draw(board: str) -> bool:
    return " " not in board


def who_won(board: list[list[str]], winner: str) -> bool:
    board_to_check = "".join(["".join(board[i]) for i in range(3)])

    if is_draw(board_to_check):
        print("Draw\n")
        return True

    if check_horizontal_lines(board_to_check) or \
            check_vertical_lines(board_to_check) or \
            check_diagonal_lines(board_to_check):
        print(f"\nPlayer with '{winner}' won\n")
        return True

    return False


def main() -> None:

    print("Welcome to the tic-tac-toe game. Good luck!")

    while True:
        game_board = [[" " for _ in range(3)] for _ in range(3)]
        free_places_to_taken = [str(i) + str(j) for i in range(3) for j in range(3)]

        while True:
            current_turn = whose_turn(free_places_to_taken)

            while True:
                print(get_board(game_board))
                print(display_free_places(free_places_to_taken))
                print(f"Now the player with '{current_turn}' chooses the position\n")
                x_position = input("Enter the horizontal position (0, 1 or 2) --> ")
                y_position = input("Enter the vertical position (0, 1 or 2) --> ")

                if x_position not in ("0", "1", "2") or y_position not in ("0", "1", "2"):
                    print("\nWrong data! Re-enter the correct data")

                else:
                    set_board(
                        game_board, free_places_to_taken,
                        int(x_position), int(y_position),
                        current_turn
                    )
                    break

            if who_won(game_board, current_turn):
                play_again = input(
                    "If you want to play again, type 'y' or "
                    "if you want to quit the game, type any character --> "
                )

                if play_again.lower() != "y":
                    print("Successful exit")
                    sys.exit(0)

                else:
                    print("\nNew board!")
                    break


if __name__ == "__main__":
    main()