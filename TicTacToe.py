class Board:
    def show():
        print()
        print(board[0], "|", board[1], "|", board[2])
        print('---------')
        print(board[3], "|", board[4], "|", board[5])
        print('---------')
        print(board[6], "|", board[7], "|", board[8])
        print()

    

class Player:
    def __init__(self, name):
        self.name = name
        
    def choose_nr(self, num1):
        self.num1 = int(input(self.name + ' please choose cell >> '))
        return self.num1

    def update_player_X(self):
        return self.board[board.index(self.name)] is 'X'

    def update_player_O(self):
        return self.board[board.index(self.name)] is 'O'


if __name__ == '__main__':
    crashed = False
    player1 = Player(input('Player 1 please insert your name: '))
    player2 = Player(input('Player 2 please insert your name: '))
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while not crashed:
        Board.show()
        print(player1.name,',', player2.name, 'welcome in the TIC-TAC-TOE game and GOOD LUCK !!!')
        print(player1.name, 'goes now!\n')
        player1.choose_nr(num1)

        print(player1.choose_nr(num1))

        break

    #inputing branch

# def input_player1():
    #     input_ok = False
#     while not input_ok:
#         player1 = int(input('Player 1 - choose cell >> '))
#         if board[(player1)-1] != 'X' and board[(player1)-1] != 'O':
#             input_ok = True
#         else:
#             print('This position is already taken... choose another one.')

