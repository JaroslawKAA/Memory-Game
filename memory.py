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

def main():

    col, row = difficulty_level()

def init_board(col, row):
    board = []
    index = 0
    
    while index < row:
        board.append([])
        index2 = 0

        while index2 < col:
            board[index].append("0")
            index2 += 1
        index += 1
    return 

if __name__ == "__main__":
    main()