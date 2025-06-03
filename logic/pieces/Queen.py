from .Piece import Piece
class Queen(Piece):
    def __init__(self, color):
        startingPosition = self.__getStartingPosition(color)
        super().__init__(color, 'queen', startingPosition, value=9)

    def __str__(self):
        return f"{self._color} queen at position {self._currentPosition}"

    def __getStartingPosition(self, color):
        if color == "white":
            return (3, 7)  
        elif color == "black":
            return (3, 0)   
        raise ValueError(f'--- ERROR(Queen.__getStartingPosition): invalid color was used ({color}) ---')
    
    def validateMove(self, newRow, newCol, boardState):
        oldCol, oldRow = self._currentPosition
        deltaCol = newCol - oldCol
        deltaRow = newRow - oldRow
        
        # --- Check if move is straight or diagonal ---
        isStraight = (deltaCol == 0 or deltaRow == 0)
        isDiagonal = (abs(deltaCol) == abs(deltaRow))
        
        if not (isStraight or isDiagonal):
            print(f'movement not permitted ({self})')
            return False
            
        # --- Determine direction of movement ---
        stepCol = 0 if deltaCol == 0 else (1 if deltaCol > 0 else -1)
        stepRow = 0 if deltaRow == 0 else (1 if deltaRow > 0 else -1)
        
        # --- Check each square along the path ---
        currentCol, currentRow = oldCol + stepCol, oldRow + stepRow
        while currentCol != newCol or currentRow != newRow:
            if boardState[currentRow][currentCol] is not None:
                print(f'pieces breaking the flow ({self})')
                return False  # Piece blocking the path
            currentCol += stepCol
            currentRow += stepRow
            
        # --- Check destination square ---
        targetPiece = boardState[newRow][newCol]
        if targetPiece is not None and targetPiece.color == self._color:
            print(f'friendly fire not permitted ({self})')
            return False  # Can't capture own piece
            
        # --- If all checks passed ---
        print(f'move approved ({self})')        
        return True