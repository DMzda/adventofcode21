with open("./input4.txt") as file:
    draw_order = [int(number) for number in file.readline().split(",")]

    boards = []
    board = []
    for line in file:
        if line.strip():
            board.append([int(number) for number in line.split()])

        if len(board) == 5:
            boards.append(board)
            board = []


def play_bingo_to_win(draw_order, boards):
    drawn = set()
    for draw in draw_order:
        drawn.add(draw)
        for board in boards:
            won = check_board(board, drawn)
            if won:
                return board, find_score(board, drawn, draw)


def play_bingo_to_lose(draw_order, boards):
    drawn = set()
    total_boards = len(boards)
    won_boards = 0

    for draw in draw_order:
        drawn.add(draw)
        for index, board in enumerate(boards):
            if not board:
                continue

            won = check_board(board, drawn)
            if won:
                won_boards += 1
                boards[index] = None
                if won_boards == total_boards:
                    return board, find_score(board, drawn, draw)


def check_board(board, drawn):
    for row in board:
        if all(number in drawn for number in row):
            return True

    for column in zip(*board):
        if all(number in drawn for number in column):
            return True


def find_score(board, drawn, last_draw):
    total_unmarked = 0
    for row in board:
        for number in row:
            if number not in drawn:
                total_unmarked += number

    return total_unmarked * last_draw


def format_board(board):
    result = ""
    for row in board:
        result += " ".join(f"{number:2}" for number in row)
        result += "\n"

    return result


if __name__ == "__main__":
    winning_board, score = play_bingo_to_win(draw_order, boards)
    print(f"Part 1\n{format_board(winning_board)}\nScore: {score}")

    losing_board, score = play_bingo_to_lose(draw_order, boards)
    print(f"Part 2\n{format_board(losing_board)}\nScore: {score}")
