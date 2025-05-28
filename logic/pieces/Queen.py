from .Piece import Piece

class Queen(Piece):
    def __init__(self, color):
        currentPosition = self.__getStartingPosition(color)
        
        # defining the initial parameters of the piece though its parent class
        super().__init__(color, currentPosition, 9, True)
        print(self.getCurrentPosition())
        
    def __str__(self):
        return f"{self.__color} queen on position {self.__currentPosition}"

    # change the initial position based out of the color of the piece
    def __getStartingPosition(self, color):
        if color == "white": 
            return "d1"
        elif color == "black":
            return "d8"
        else: # managing input errors (for debugging)
            print("--- ERROR: invalid color was used (use white and black as keyword) ---")

    # def getCurrentPosition(self):
    #     return self.__currentPosition