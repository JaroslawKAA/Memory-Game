import os
import string
import random
from colorama import *
from copy import deepcopy
import winsound

def difficulty_level():
    print(""" 
    
    Choose difficulty level!: 
    
    1. Easy
    2. Medium
    3. Hard""")

    choice = input("Your pick is: ")
    winsound.Beep(500, 150)

    while choice not in ["1", "2", "3"]:
        print("Choose correct answer (1, 2 or 3)")
        choice = input("Your pick is: ")
        winsound.Beep(500, 150)
    if choice == "1":
        return 5, 4
    elif choice == "2":
        return 5, 6
    elif choice == "3":
        return 5, 10


def get_random_letters(letters, board):
    letters_list = [char for char in letters]
    letters_list.extend(letters_list)
    random.shuffle(letters_list)
    index = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = letters_list[index]
            index += 1

def color_string(color, string):
    return color + string + Fore.RESET

def color_board(color, board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != "#":
                board[i][j] = color_string(color, board[i][j])

            

def display_board(board):
    length = len(board[0])
    header = color_string(Fore.BLUE, string.ascii_uppercase[:length])

    print("\n  " + header)

    index = 1

    temp_board = deepcopy(board) 

    color_board(Fore.GREEN, temp_board)

    for row in temp_board:
        row_to_print = color_string(Fore.BLUE, str(index)) + " " + "".join(row)
        print(row_to_print)
        index += 1


def get_coords(col, row):
    cols = string.ascii_lowercase[:col]
    rows = list(range(row))
    rows = list(map(lambda x: str(x + 1), rows))

    user_input = input("Provide your coords (Eg. a1, b4, etc...): ")
    winsound.Beep(500, 150)
    while len(user_input) != 2 or user_input[0].lower() not in cols or user_input[1] not in rows:
        print("Incorrect answer. Try again!")
        user_input = input("Provide your coords (Eg. a1, b4, etc...): ")
        winsound.Beep(500, 150)

    x = ord(user_input[0].lower()) - 97
    y = int(user_input[1]) - 1
    return y, x


def uncover_item(hidden_board, visible_board, coords):
    row = coords[0]
    col = coords[1]
    if visible_board[row][col] != "#":
        raise ValueError("You try check the same element again!")
    visible_board[row][col] = hidden_board[row][col]


def hash_items(coords1, coords2, board):
    board[coords1[0]][coords1[1]] = '#'
    board[coords2[0]][coords2[1]] = '#'


def has_won(board):
    for row in board:
        for item in row:
            if item == '#':
                return False
    return True


def main():
    col, row = difficulty_level()
    hidden_board = init_board(col, row)
    visible_board = init_board(col, row)
    amount_of_letters = int(col * row / 2)
    letters = string.ascii_lowercase[:amount_of_letters]
    get_random_letters(letters, hidden_board)
    while not has_won(visible_board):
        os.system("cls || clear")
        display_board(visible_board)

        coords1 = get_coords(col, row)
        uncover_item(hidden_board, visible_board, coords1)
        os.system("cls || clear")
        display_board(visible_board)

        coords2 = get_coords(col, row)
        uncover_item(hidden_board, visible_board, coords2)
        os.system("cls || clear")
        display_board(visible_board)

        if visible_board[coords1[0]][coords1[1]] != visible_board[coords2[0]][coords2[1]]:
            hash_items(coords1, coords2, visible_board)
            input(Fore.RED + "Letters unmatched! Try again! Press ENTER to continue... " + Fore.RESET)
        else:
            input(Fore.GREEN + "Congratulations! U hit a pair of items! Press ENTER to continue... " + Fore.RESET)



def init_board(col, row):
    board = []
    index = 0

    while index < row:
        board.append([])
        index2 = 0

        while index2 < col:
            board[index].append("#")
            index2 += 1
        index += 1
    return board


if __name__ == "__main__":
    main()
