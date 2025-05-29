from .Piece import Piece

class Pawn(Piece):
    def __init__(self, color, number):
        startingPosition = self.__getStartingPosition(color, number)
        imgName = self.__getImgName(color)
        self.__number = number

        # defining the initial parameters of the piece though its parent class
        super().__init__(color, startingPosition, 1, imgName)
        
    def __str__(self):
        return f"{self._color} pawn n° {self.__number} on position {self._currentPosition}"

    # change the initial position based out of the color of the piece
    def __getStartingPosition(self, color, number):
        xPositions = (0,1,2,3,4,5,6,7)
        xPos = xPositions[number]
        
        if color == "white": 
            yPos = 6
        elif color == "black": 
            yPos = 1
        else:
            raise ValueError(f"--- ERROR(Pawn.__getStartingPosition): invalid color was used ({color}) ---")
        return (xPos, yPos)
    
    def __getImgName(self, color):
        # get the name of the img based on color
        if color == "white":
            return 'white-pawn.png'  
        elif color == "black":
            return 'black-pawn.png'
        raise ValueError(f'--- ERROR(Pawn.__getImgName): invalid color was used ({color}) ---')