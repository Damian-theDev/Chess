from .Piece import Piece
class Knight(Piece):
    def __init__(self, color, number):
        startingPosition = self.__getStartingPosition(color, number)
        self.__number = number

        # defining the initial parameters of the piece though its parent class
        super().__init__(color, 'knight', startingPosition, value=3)

    def __str__(self):
        return f"{self._color} knight n° {self.__number} on position {self._currentPosition}"

    # change the initial position based out of the color of the piece
    def __getStartingPosition(self, color, number):
        xPositions = (1, 6)
        xPos = xPositions[number]
        
        if color == "white": 
            yPos = 7
        elif color == "black": 
            yPos = 0
        else:
            raise ValueError(f"--- ERROR(Knight.__getStartingPosition): invalid color was used ({color}) ---")
        return (xPos, yPos)
    
    def validateMove(self, newRow, newCol, boardState):
        oldCol, oldRow = self._currentPosition
        deltaCol = abs(newCol - oldCol)
        deltaDiff = abs(newRow - oldRow)
    
        # --- Knight moves in L-shape (2-1 pattern) ---
        if not ((deltaCol == 2 and deltaDiff == 1) or (deltaCol == 1 and deltaDiff == 2)):
            print(f'movement not permitted ({self})')
            return False
            
        # --- Check destination square ---
        targetPiece = boardState[newRow][newCol]
        if targetPiece is not None and targetPiece.color == self._color:
            print(f'friendly fire is not permitted ({self})')
            return False  # Can't capture own piece
            
        self._currentPosition = (newCol, newRow)
        print(f'move approved ({self})')        
        return True