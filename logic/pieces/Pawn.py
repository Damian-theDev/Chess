from .Piece import Piece

class Pawn(Piece):
    def __init__(self, color, number):
        # TODO - fix the init, make it like the queen class' one
        self.__color = color
        self.__number = number
        self.__currentPosition = self.__getStartingPosition()
        self.__value = 9
        self.__statusAlive = True

        # defining the initial parameters of the piece though its parent class
        super().__init__(self.__currentPosition, self.__value, self.__statusAlive)

    def __str__(self):
        return f"{self.__color} pawn on position {self.__currentPosition}"

    # change the initial position based out of the color of the piece
    def __getStartingPosition(self):
        letters = ('a','b','c','d','e','f','g','h')
        pos = letters[self.__number]
        
        if self.__color == "white": 
            pos += "7"
        elif self.__color == "black": 
            pos += "2"
        else:
            print("--- ERROR: invalid color was used (use white and black as keyword) ---")