import time
import random

def rules():
    print("The board will look like this!")
    print("The positions of this 3 x 3 board is same as the right side of your key board.\n")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    print("\nYou just have to input the position(1-9).")


def names():
    #Player names input;
    
    p1_name=input("\nEnter NAME of PLAYER 1:\t").capitalize()
    p2_name=input("Enter NAME of PLAYER 2:\t").capitalize()
    return (p1_name, p2_name)


def choice():
    p1_choice = ' '
    p2_choice = ' '
    while p1_choice != 'X' or p1_choice != 'O':

        p1_choice = input(f"\n{p1_name}, Do you want to be X or O?\t")[0].upper()

        if p1_choice == 'X' or p1_choice == 'O':
            break
        print("INVALID INPUT! Please Try Again!") 

    if p1_choice == 'X':
        p2_choice = 'O'
    elif p1_choice == 'O':
        p2_choice = 'X'
    
    return (p1_choice, p2_choice)



def first_player():
    return random.choice((0, 1))


def display_board(board, avail):
    print("    " + " {} | {} | {} ".format(board[7],board[8],board[9]) + "            " + " {} | {} | {} ".format(avail[7],avail[8],avail[9]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[4],board[5],board[6]) + "            " + " {} | {} | {} ".format(avail[4],avail[5],avail[6]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[1],board[2],board[3]) + "            " + " {} | {} | {} ".format(avail[1],avail[2],avail[3]))


def player_choice(board, name, choice):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(f'\n{name} ({choice}), Choose your next position: (1-9) \t'))
        
        if position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position) or position == "": 
            print(f"INVALID INPUT. Please Try Again!\n")   
    print("\n")        
    return position


def CompAI(board, name, choice):
    position = 0
    possibilities = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    
    # including both X and O, since if computer will win, he will place a choice there, but if the component will win --> we have to block that move
    for let in ['O', 'X']:
        for i in possibilities:
            # Creating a copy of the board everytime, placing the move and checking if it wins;
            # Creating a copy like this  and not this boardCopy = board, since changes to boardCopy changes the original board;
            boardCopy = board[:]
            boardCopy[i] = let
            if(win_check(boardCopy, let)):
                position = i
                return position

    openCorners = [x for x in possibilities if x in [1, 3, 7, 9]]
    
    if len(openCorners) > 0:
        position = selectRandom(openCorners)
        return position

    if 5 in possibilities:
        position = 5
        return position

    openEdges = [x for x in possibilities if x in [2, 4, 6, 8]]
    
    if len(openEdges) > 0:
        position = selectRandom(openEdges)
        return position



def selectRandom(board):
    import random
    ln = len(board)
    r = random.randrange(0,ln)
    return board[r]


def place_marker(board, avail, choice, position):
    #To mark/replace the position on the board list;
    board[position] = choice
    avail[position] = ' '


def space_check(board, position):
    #To check whether the given position is empty or occupied;
    return board[position] == ' '


def full_board_check(board):
    #To check if the board is full, then the game is a draw;
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def win_check(board, choice):    
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9), # horizontals
        (1, 4, 7), (2, 5, 8), (3, 6, 9), # verticals
        (1, 5, 9), (3, 5, 7)             # diagonals
    ]
    for x, y, z in win_conditions:
        if board[x] == board[y] == board[z] == choice:
            return True
    return False
def replay():
    #If the users want to play the game again?
    return input('\nDo you want to play again? Enter [Y]es or [N]o: ').lower().startswith('y')

rules()


while True:
    theBoard = [' ']*10
    available = [str(num) for num in range(0,10)]

    print("\n[0]. Player vs. Computer")
    print("[1]. Player vs. Player")
    print("[2]. Computer vs. Computer")
    mode = int(input("\nSelect an option [0]-[2]: "))
    if mode == 1:
        p1_name, p2_name = names()
        p1_choice, p2_choice = choice()
        print(f"\n{p1_name}:", p1_choice)
        print(f"{p2_name}:", p2_choice)

    elif mode == 0:
        p1_name = input("\nEnter NAME of PLAYER who will go against the Computer:\t").capitalize()
        p2_name = "Computer"

        p1_choice, p2_choice = choice()
        print(f"\n{p1_name}:", p1_choice)
        print(f"{p2_name}:", p2_choice)
    
    else:
        p1_name = "Computer1"
        p2_name = "Computer2"
        p1_choice, p2_choice = "X", "O"
        print(f"\n{p1_name}:", p1_choice)
        print(f"\n{p2_name}:", p2_choice)

    if first_player():
        turn = p2_name
    else:
        turn = p1_name

    print(f"\n{turn} will go first!")
    
    play_game = True
    if(mode == 2):
        play_game = 1
    
    while play_game:
        if turn == p1_name:
            
            display_board(theBoard, available)

            if mode != 2:
                position = player_choice(theBoard, p1_name, p1_choice)
            else:
                position = CompAI(theBoard, p1_name, p1_choice)
                print(f'\n{p1_name} ({p1_choice}) has placed on {position}\n')
            
            place_marker(theBoard, available, p1_choice, position)

            if win_check(theBoard, p1_choice):
                display_board(theBoard, available)
                if(mode):
                    print(f'\n\nCONGRATULATIONS {p1_name}! YOU WON!\n\n')
                else:
                    print('\n\nTHE Computer HAS WON THE GAME!\n\n')
                play_game = False
                
            else:
                if full_board_check(theBoard):
                    display_board(theBoard, available)
                    print('\nThe game is a DRAW!\n')
                    break
                else:
                    turn = p2_name
                          
        elif turn == p2_name:
            display_board(theBoard, available)
            if(mode == 1):
                position = player_choice(theBoard, p2_name, p2_choice)
            else:
                position = CompAI(theBoard, p2_name, p2_choice)
                print(f'\n{p2_name} ({p2_choice}) has placed on {position}\n')
            
            place_marker(theBoard, available, p2_choice, position)
            
            if win_check(theBoard, p2_choice):
                display_board(theBoard, available)
                if(mode):
                    print(f'\n\nCONGRATULATIONS {p2_name}! YOU WON!\n\n')
                else:
                    print('\n\nTHE Computer HAS WON THE GAME!\n\n')
                play_game = False
                
            else:
                if full_board_check(theBoard):
                    display_board(theBoard, available)
                    print('\nThe game is a DRAW!\n')
                    break
                else:
                    turn = p1_name
             
    if replay():
        continue
    else:
        break