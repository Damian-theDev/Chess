class Board():
    def __init__(self):
        self.__board = [[None for _ in range(8)] for _ in range(8)]

    # puts a piece in a specified position on the board
    def addPiece(self, piece, position):
        if isinstance(position, tuple):
            self.__board[int(position[0])][int(position[1])] = piece
        else:
            print('--- ERROR(Board.addPiece): position was not specified the right way ---')
            
    # printing the board    
    def printBoard(self):
        for pos, i in enumerate(self.__board):
            print(pos ,i)

    # resetting the board to the initial condition
    def resetBoard(self):
        self.__board = [
            [None, None, None, None, None, None, None, None], 
            [None, None, None, None, None, None, None, None], 
            [None, None, None, None, None, None, None, None], 
            [None, None, None, None, None, None, None, None], 
            [None, None, None, None, None, None, None, None], 
            [None, None, None, None, None, None, None, None], 
            [None, None, None, None, None, None, None, None], 
            [None, None, None, None, None, None, None, None]
        ]
    
    def getBoard(self, position=None):
        if position:
            return self.__board[position[0]][position[1]]
        return self.__board