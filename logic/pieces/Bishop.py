from .Piece import Piece
class Bishop(Piece):
    def __init__(self, color, number):
        startingPosition = self.__getStartingPosition(color, number)
        self.__number = number
    
        # defining the initial parameters of the piece though its parent class
        super().__init__(color, 'bishop', startingPosition, value=3)

    def __str__(self):
        return f"{self._color} bishop n° {self.__number} at position {self._currentPosition}"

    # change the initial position based out of the color of the piece
    def __getStartingPosition(self, color, number):
        xPositions = (2, 5)
        xPos = xPositions[number]
        
        if color == "white": 
            yPos = 7
        elif color == "black": 
            yPos = 0
        else:
            raise ValueError(f"--- ERROR(Bishop.__getStartingPosition): invalid color was used ({color}) ---")
        return (xPos, yPos)
    
    def validateMove(self, newRow, newCol, boardState):
        oldCol, oldRow = self._currentPosition
        deltaCol = newCol - oldCol
        deltaRow = newRow - oldRow
        
        # --- check if move is diagonal ---
        isDiagonal = (abs(deltaCol) == abs(deltaRow))
        if not isDiagonal:
            return False
            
        # --- Determine direction of movement ---
        stepCol = 0 if deltaCol == 0 else (1 if deltaCol > 0 else -1)
        stepRow = 0 if deltaRow == 0 else (1 if deltaRow > 0 else -1)
        
        # --- Check each square along the path ---
        currentCol, currentRow = oldCol + stepCol, oldRow + stepRow
        while currentCol != newCol or currentRow != newRow:
            if boardState[currentRow][currentCol] is not None:
                return False  # Piece blocking the path
            currentCol += stepCol
            currentRow += stepRow
            
        # --- Check destination square ---
        targetPiece = boardState[newRow][newCol]
        if targetPiece is not None and targetPiece.color == self._color:
            return False  # Can't capture own piece
            
        # --- If all checks passed ---
        return True