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
        targetPiece = boardState[newRow][newCol]

        # --- normal king movement rules ---
        if colDiff > 1 or rowDiff > 1:
            if not self.__validateCastling(newRow, newCol, boardState):
                return False
                    
        # --- friendly fire not permitted ---
        if targetPiece is not None and targetPiece.color == self._color:
            return False
        
        # --- don't put yourself in check ---
        if self.__squareIsSafe(newCol, newRow, boardState):
            return True

        return False

    def __validateCastling(self, newRow, newCol, boardState):
        oldCol, oldRow = self._currentPosition
        
        # --- king has already moved ---
        if not self._firstMove:
            return False
        
        # --- must be moving horizontally ---
        if newRow != oldRow:
            return False
        
        # --- must be moving exactly 2 squares ---
        if abs(newCol - oldCol) != 2:
            return False
        
        # --- determine rook position and direction ---
        direction = 2 if newCol > oldCol else -2  # kingside (2) or queenside (-2)
        rookCol = 7 if direction == 2 else 0
        rook = boardState[oldRow][rookCol]
        
        # --- rook conditions ---
        if not (rook and rook.type == 'rook' and rook._firstMove):
            print(1)
            return False
        
        # --- check if squares between are empty ---
        start = min(oldCol, newCol) + 1
        end = max(oldCol, newCol)
        for col in range(start, end):
            if boardState[oldRow][col] is not None:
                print(2)
                return False
        
        # --- check if king moves through check ---
        for col in [oldCol, oldCol + direction, newCol]:
            if not self.__squareIsSafe(col, oldRow, boardState):
                print(3)
                return False
        
        # --- castle approved ---
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