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
    
    # initialise a board in a specific condition
    def setBoard(self, boardState):
        self.__board = boardState
        
    # def movePiece(self, initCol, )

    # resetting the board to the initial condition
    def resetBoard(self):
        self.__board = [[None for _ in range(8)] for _ in range(8)]
    
    def getBoard(self, position=None):
        if position and isinstance(position, tuple) and len(position) == 2:
            return self.__board[position[0]][position[1]]
        return self.__board
    
    
    
    
    def print_board_debug(self):
        piece_symbols = {
            'pawn': '♟', 'rook': '♜', 'knight': '♞',
            'bishop': '♝', 'queen': '♛', 'king': '♚'
        }
        
        print("  a b c d e f g h")
        print(" +-----------------+")
        for row in range(8):
            print(f"{8-row}|", end="")
            for col in range(8):
                piece = self.getBoard()[row][col]
                if piece:
                    color_code = '\033[94m' if piece.color == 'white' else '\033[91m'
                    print(f"{color_code}{piece_symbols[piece.type]}\033[0m", end=" ")
                else:
                    print("·", end=" ")
            print(f"|{8-row}")
        print(" +-----------------+")
        print("  a b c d e f g h")