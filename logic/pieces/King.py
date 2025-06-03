from .Piece import Piece
class King(Piece):
    def __init__(self, color):
        startingPosition = self.__getStartingPosition(color)
        super().__init__(color, 'king', startingPosition, value=0)  # Highest value piece

    def __str__(self):
        return f"{self._color} king at position {self._currentPosition}"

    def __getStartingPosition(self, color):
        if color == "white":
            return (4, 7)
        elif color == "black":
            return (4, 0)
        raise ValueError(f'--- ERROR(King.__getStartingPosition): invalid color was used ({color}) ---')

    def validateMove(self, newRow, newCol, boardState):
        oldCol, oldRow = self._currentPosition
        colDiff = abs(newCol - oldCol)
        rowDiff = abs(newRow - oldRow)

        # --- normal king movement rules ---
        if colDiff > 1 or rowDiff > 1:
            print(f'movement not permitted ({self})')
            return False
        
        targetPiece = boardState[newRow][newCol]
            
        if targetPiece is not None and targetPiece.color == self._color:
            print(f'friendly fire is not permitted ({self})')
            return False
        
        if self.__squareIsSafe(newCol, newRow, boardState):
            print(f'move approved ({self})')  
            return True
            

    #     # --- castling ---
    #     if self.firstMove and rowDiff == 0 and colDiff == 2:
    #         return self.__validateCastling(newCol, boardState)
    #     return False

    # def __validateCastling(self, newCol, boardState):
    #     oldCol, oldRow = self._currentPosition
    #     direction = 1 if newCol > oldCol else -1  # Kingside or queenside
    #     rookCol = 7 if direction == 1 else 0
        
    #     # check if rook exists and hasn't moved
    #     rook = boardState[oldRow][rookCol]
    #     if not rook or rook.type != 'rook' or rook.color != self._color or (rook.firstMove == False):
    #         return False
            
    #     # check if squares between are empty
    #     for col in range(min(oldCol, rookCol) + 1, max(oldCol, rookCol)):
    #         if boardState[oldRow][col] is not None:
    #             return False
                
    #     # check if king would move through check
    #     for col in range(oldCol, oldCol + direction*2, direction):
    #         if self.__isSquareUnderAttack(oldRow, col, boardState, self._color):
    #             return False
                
    #     return True

    def __squareIsSafe(self, newKingCol, newKingRow, boardState):
        # check if any opponent piece attacks this square
        for checkedRow in range(8):
            for checkedCol in range(8):
                piece = boardState[checkedCol][checkedRow]
                
                # empty cell, no threats
                if piece == None:
                    continue 
                    
                # same color, no threats
                if piece.color == self._color:
                    continue
                
                # check if the enemy piece is a threat
                if piece.type == 'pawn' and piece.canAttack(newKingRow, newKingCol, boardState):
                    return False
                elif piece.validateMove(newKingRow, newKingCol, boardState):
                    return False
            


        return True