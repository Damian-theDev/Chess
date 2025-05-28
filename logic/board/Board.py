class Board():
    def __init__(self):
        self.__board = [[None for _ in range(8)] for _ in range(8)]

    # TODO - evaluate if this method is actually required
    # puts a piece in a specified position on the board
    def addPiece(self, piece, position):
        if isinstance(position, str):
            self.__board[int(position[0])][int(position[1])] = piece

    # printing the board    
    def printBoard(self):
        letters = ('a','b','c','d','e','f','g','h')
        for pos, i in enumerate(self.__board):
            print(pos ,i)

    # TODO - check if this method is fine as here defined, might consider setting up the pieces since the starting
    # resetting the board to the initial condition
    def __resetBoard(self):
        self.__board = [
            ['a8', None, None, None, None, None, None, 'h8'], 
            [None, None, None, None, None, None, None, None], 
            [None, None, None, None, None, None, None, None], 
            [None, None, None, None, None, None, None, None], 
            [None, None, None, None, None, None, None, None], 
            [None, None, None, None, None, None, None, None], 
            [None, None, None, None, None, None, None, None], 
            ['a1', None, None, None, None, None, None, 'h1']
        ]
    
    def getBoard(self):
        return self.__board