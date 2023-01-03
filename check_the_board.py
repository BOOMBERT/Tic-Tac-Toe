def check_horizontal_lines(board_lines: str) -> bool:
    first_line = board_lines[:3]
    second_line = board_lines[3:6]
    third_line = board_lines[6:9]

    return checking_for_win(first_line, second_line, third_line)


def check_vertical_lines(board_lines: str) -> bool:
    first_line = board_lines[::3]
    second_line = board_lines[1::3]
    third_line = board_lines[2::3]

    return checking_for_win(first_line, second_line, third_line)


def check_diagonal_lines(board_lines: str) -> bool:
    first_line = board_lines[::4]
    second_line = board_lines[-3::-2][:3]

    return checking_for_win(first_line, second_line)


def checking_for_win(*args: str) -> bool:
    return any(line in ("OOO", "XXX") for line in args)


def is_draw(board_lines: str) -> bool:
    return " " not in board_lines
