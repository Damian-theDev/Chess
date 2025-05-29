from .Piece import Piece
class Queen(Piece):
    def __init__(self, color):
        startingPosition = self.__getStartingPosition(color)

        # defining the initial parameters of the piece though its parent class
        super().__init__(color, startingPosition, value=9)

    def __str__(self):
        return f"{self._color} queen at position {self._currentPosition}"

    def __getStartingPosition(self, color):
        # determine the starting position based on color
        if color == "white":
            return (4, 7)  
        elif color == "black":
            return (4, 0)   
        raise ValueError(f'--- ERROR(Queen.__getStartingPosition): invalid color was used ({color}) ---')