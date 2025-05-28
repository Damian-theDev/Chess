from .Piece import Piece

class Pawn(Piece):
    def __init__(self, color, number):
        currentPosition = self.__getStartingPosition(color, number)
        self.__number = number

        # defining the initial parameters of the piece though its parent class
        super().__init__(color, currentPosition, 1, True)

    def __str__(self):
        return f"{self.__color} pawn n° s{self.__number} on position {self.__currentPosition}"

    # change the initial position based out of the color of the piece
    def __getStartingPosition(self, color, number):
        letters = ('a','b','c','d','e','f','g','h')
        pos = letters[number]
        
        if color == "white": 
            pos += "7"
        elif color == "black": 
            pos += "2"
        else:
            print("--- ERROR(Pawn.__getStartingPosition): invalid color was used (use white and black as keyword) ---")