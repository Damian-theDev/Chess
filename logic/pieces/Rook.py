from .Piece import Piece

class Rook(Piece):
    def __init__(self, color, number):
        startingPosition = self.__getStartingPosition(color, number)
        self.__number = number

        # defining the initial parameters of the piece though its parent class
        super().__init__(color, 'rook', startingPosition, value=5)
        
    def __str__(self):
        return f"{self._color} rook n° {self.__number} on position {self._currentPosition}"

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
    
    def validateMove(self, newRow, newCol, boardState):
        oldCol, oldRow = self._currentPosition
        deltaCol = newCol - oldCol
        deltaRow = newRow - oldRow
        
        # --- check if move is straight or diagonal ---
        isStraight = (deltaCol == 0 or deltaRow == 0)
        
        if not isStraight:
            print(f'movement not permitted ({self})')
            return False
            
        # --- determine direction of movement ---
        stepCol = 0 if deltaCol == 0 else (1 if deltaCol > 0 else -1)
        stepRow = 0 if deltaRow == 0 else (1 if deltaRow > 0 else -1)
        
        # --- check each square along the path ---
        currentCol, currentRow = oldCol + stepCol, oldRow + stepRow
        while currentCol != newCol or currentRow != newRow:
            if boardState[currentRow][currentCol] is not None:
                print(f'pieces breaking the flow ({self})')
                return False  # Piece blocking the path
            currentCol += stepCol
            currentRow += stepRow
            
        # --- check destination square ---
        targetPiece = boardState[newRow][newCol]
        if targetPiece is not None and targetPiece.color == self._color:
            print(f'friendly fire not permitted ({self})')
            return False  
            
        # --- if all checks passed ---
        print(f'move approved ({self})') 
        return True