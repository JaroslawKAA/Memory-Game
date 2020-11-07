import string
import random


def difficulty_level():
    print(""" 
    
    Choose difficulty level!: 
    
    1. Easy
    2. Medium
    3. Hard""")

    choice = input("Your pick is: ")

    while choice not in ["1", "2", "3"]:
        print("Choose correct answer (1, 2 or 3)")
        choice = input("Your pick is: ")

    if choice == "1":
        return 5, 4
    elif choice == "2":
        return 5, 6
    elif choice == "3":
        return 5, 10


def get_random_letters(letters, board):
    letters_list = [char for char in letters]
    random.shuffle(letters_list)
    index = 0
    last_index = len(letters_list)

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = letters_list[index]
            index += 1
            if index >= last_index:
                index = 0
                random.shuffle(letters_list)


def main():
    col, row = difficulty_level()
    hidden_board = init_board(col, row)
    visible_board = init_board(col, row)
    amount_of_letters = int(col * row / 2)
    letters = string.ascii_lowercase[:amount_of_letters]
    get_random_letters(letters, hidden_board)


def init_board(col, row):
    board = []
    index = 0

    while index < col:
        board.append([])
        index2 = 0

        while index2 < row:
            board[index].append("#")
            index2 += 1
        index += 1
    return board


if __name__ == "__main__":
    main()
