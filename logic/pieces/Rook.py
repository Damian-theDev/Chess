from .Piece import Piece

class Rook(Piece):
    def __init__(self, color, number):
        startingPosition = self.__getStartingPosition(color, number)
        imgName = self.__getImgName(color)
        self.__number = number

        # defining the initial parameters of the piece though its parent class
        super().__init__(color, startingPosition, 5, imgName)
        
    def __str__(self):
        return f"{self._color} rook n° s{self.__number} on position {self._currentPosition}"

    # change the initial position based out of the color of the piece
    def __getStartingPosition(self, color, number):
        xPositions = (0, 7)
        xPos = xPositions[number]
        
        if color == "white": 
            yPos = 7
        elif color == "black": 
            yPos = 0
        else:
            raise ValueError(f"--- ERROR(Rook.__getStartingPosition): invalid color was used ({color}) ---")
        return (xPos, yPos)
    
    def __getImgName(self, color):
        # get the name of the img based on color
        if color == "white":
            return 'white-rook.png'  
        elif color == "black":
            return 'black-rook.png'
        raise ValueError(f'--- ERROR(Rook.__getImgName): invalid color was used ({color}) ---')