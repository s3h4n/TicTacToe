# Tic Tac Toe Game in Python
# Author: S3H4N
# GitHub: https://github.com/s3h4n/tictactoe


# Import required modules
import random
import sys

# Global variables
empty = " "
board = [empty] * 9
player_one = "X"
player_two = "O"


def draw_board(board: list) -> None:
    """
    draw_board function draws the board.

    Args:
        board (list): The board to be drawn.
    """

    print("")

    for position in range(0, len(board), 3):

        print(f" {board[position]} | {board[position+1]} | {board[position+2]} ")

        if position != 6:
            print("---+---+---")


def empty_position(board: list, postion: int) -> bool:
    """
    empty_position function checks if a position is empty.

    Args:
        board (list): The board to be checked.
        postion (int): The position to be checked.

    Returns:
        bool: True if the position is empty, False otherwise.
    """

    return True if board[postion] == empty else False


def valid_move(board: list, position: int, player: str) -> bool:
    """
    valid_move function checks if a move is valid. And apply if its valid.

    Args:
        board (list): The board to be checked.
        position (int): The position to be checked.
        player (str): The player to be checked.

    Returns:
        bool: True if the move is valid, False otherwise.
    """

    if empty_position(board, position):

        board[position] = player
        return True

    return False


def check_winner(board: list) -> str:
    """
    check_winner function checks if there is a winner.

    Args:
        board (list): The board to be checked.

    Returns:
        str: The winner if there is one, empty otherwise.
    """

    patterns = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for pattern in patterns:

        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != empty:
            return board[pattern[0]]

    return empty


def print_winner(board: list) -> None:
    """
    print_winner function prints the winner.

    Args:
        board (list): [description]
    """

    if check_winner(board) == player_one:
        print(f"\nPlayer {player_one} wins")

    elif check_winner(board) == player_two:
        print(f"\nPlayer {player_two} wins")

    elif check_winner(board) == empty:
        print("\nIt's a tie")


def random_positon() -> int:
    """
    random_positon function returns a random position.

    Returns:
        int: A random position.
    """

    return random.randint(0, 8)


def best_position(board: list) -> int:
    """
    best_position function returns the best position for the computer.

    Args:
        board (list): The board to be checked.

    Returns:
        int: The best position for the computer.
    """

    available_positions = [
        x for x, letter in enumerate(board) if letter == empty and x != 0
    ]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

    best_position = 0

    # Check for winning move
    for let in [player_one, player_two]:

        for position in available_positions:
            board_copy = board.copy()
            board_copy[position] = let

            if check_winner(board_copy) == let:
                best_position = position
                return best_position

    # Check for blocking move
    corner_positions = [
        position for position in available_positions if position in [0, 2, 6, 8]
    ]

    if len(corner_positions) > 0:
        return random.choice(corner_positions)

    # Check for center position
    if 5 in available_positions:
        return 5

    # Check for empty side positions
    edge_positions = [
        position for position in available_positions if position in [1, 3, 5, 7]
    ]

    if len(edge_positions) > 0:
        return random.choice(edge_positions)


def computer_move(board: list, player: str) -> int:
    """
    computer_move function applies the computer move.

    Args:
        board (list): The board to be checked.
        player (str): The player to be checked.

    Returns:
        int: The best position for the computer.
    """

    position = best_position(board)

    if not valid_move(board, position, player):
        computer_move(board, player)
    else:
        print("\nComputer's move: ", position + 1)


def human_move(board: list, player: str) -> int:
    """
    human_move function applies the human move.

    Args:
        board (list): The board to be checked.
        player (str): The player to be checked.

    Returns:
        int: The best position for the computer.
    """

    position = int(input("\nEnter a position: "))

    if position > 9 or position < 0:
        print("\nInvalid position")
        human_move(board, player)

    elif not valid_move(board, position - 1, player):
        print("\nInvalid position")
        human_move(board, player)


def play_game() -> None:
    """
    play_game function plays the game.
    """

    for i in range(0, 9):
        if check_winner(board) != empty:
            break

        draw_board(board)

        if i % 2 == 0:  # If it's player one's turn
            human_move(board, player_one)
        else:  # If it's player two's turn
            computer_move(board, player_two)


def banner() -> None:
    """
    banner function prints the banner.
    """

    print("\nTic Tac Toe")
    print(f"\nplayer_one is {player_one} and player_two is {player_two}")


def main() -> None:
    """
    main function runs the game.
    """

    try:  # Try to run the game
        banner()
        play_game()
        draw_board(board)
        print_winner(board)

    except KeyboardInterrupt:  # If the user presses Ctrl+C
        print("\nGoodbye!")
        sys.exit()

    except Exception as e:  # If there is an error
        print(e)


if __name__ == "__main__":  # If the program is run directly
    main()
