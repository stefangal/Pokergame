import os


class Board:
    global board
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def show():
        print()
        print(board[0], "|", board[1], "|", board[2])
        print('---------')
        print(board[3], "|", board[4], "|", board[5])
        print('---------')
        print(board[6], "|", board[7], "|", board[8])
        print()

    def check_winner(self):
        pass
    
class Player:
    def __init__(self, name):
        self.name = name

    def choose_nr(self):   
        global num1
        good_input = False
        while good_input == False:
            num1 = int(input(self.name + ' please choose cell 1-9 > '))
            if board[(num1)-1] != 'X' or board[board(num1)-1] != 'O':
                good_input = True
                return num1
            else: 
                print('This position is already taken... choose another one.')    

    def player_gives_OX(self):
        if self.name == player1.name and board[(num1)-1] != 'X' or board[board(num1)-1] != 'O':
            board[board.index(num1)] = 'O'
        elif self.name == player2.name and board[(num1)-1] != 'X' or board[board(num1)-1] != 'O':
            board[board.index(num1)] = 'X'

if __name__ == '__main__':
    os.system("cls")
    crashed = False
    print("Tic Tac Toe game...\n")
    player1 = Player(input('Player 1 please insert your name: '))
    player2 = Player(input('Player 2 please insert your name: '))
    os.system("cls")
    print(player1.name,',', player2.name, 'welcome in the TIC-TAC-TOE game and GOOD LUCK !!!')
    print(player1.name, "goes now with 'O'!", player2.name,"goes wih 'X' \n")
    while not crashed:
        Board.show()
        player1.choose_nr()
        player1.player_gives_OX()
        os.system("cls")
        print(player1.name,',', player2.name, 'welcome in the TIC-TAC-TOE game and GOOD LUCK !!!')
        print(player1.name, "goes now with 'O'!", player2.name,"goes wih 'X' \n")
        Board.show()
        player2.choose_nr()
        player2.player_gives_OX()
        os.system("cls")
        print(player1.name,',', player2.name, 'welcome in the TIC-TAC-TOE game and GOOD LUCK !!!')
        print(player1.name, "goes now with 'O'!", player2.name,"goes wih 'X' \n")
        
    # def choose_nr(self):   
    #     global num1
    #     num1 = int(input(self.name + ' please choose cell 1-9 > '))
    #     return num1



# def input_player1():
    #     input_ok = False
#     while not input_ok:
#         player1 = int(input('Player 1 - choose cell >> '))
#         if board[(player1)-1] != 'X' and board[(player1)-1] != 'O':
#             input_ok = True
#         else:
#             print('This position is already taken... choose another one.')


