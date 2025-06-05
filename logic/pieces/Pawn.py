from .Piece import Piece

class Pawn(Piece):
    def __init__(self, color, number):
        startingPosition = self.__getStartingPosition(color, number)
        self.__number = number
        self.__en_passant_vulnerable = False

        # defining the initial parameters of the piece though its parent class
        super().__init__(color, 'pawn', startingPosition, value=1)
        
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
    
    def validateMove(self, newRow, newCol, boardState):
        self.__en_passant_vulnerable = False
        oldCol, oldRow = self._currentPosition
        direction = -1 if self._color == "white" else 1  # White moves up, black moves down
        
        # --- movement rules ---
        # default movement
        if (newCol == oldCol and 
            newRow == oldRow + direction and 
            boardState[newRow][newCol] is None):
            return True
            
        # double step from starting position
        if (self._firstMove and 
            newCol == oldCol and 
            newRow == oldRow + 2*direction and 
            boardState[oldRow + direction][oldCol] is None and 
            boardState[newRow][newCol] is None):
            self.__en_passant_vulnerable = True
            return True
        
        # attacking
        if self.canAttack(newRow, newCol, boardState):
            return True
        
        return False
            
    # --- capture rules ---
    def canAttack(self, newRow, newCol, boardState):
        oldCol, oldRow = self._currentPosition
        direction = -1 if self._color == "white" else 1  # White moves up, black moves down
        
        if (abs(newCol - oldCol) == 1 and 
            newRow == oldRow + direction):
            
            # standard capture
            if (boardState[newRow][newCol] and 
                boardState[newRow][newCol].color != self._color):
                return True
                
            # TO IMPLEMENT : en passant capture
            # adjacent_piece = boardState[oldRow][newCol]
            # if (adjacent_piece and 
            #     adjacent_piece.type == 'pawn' and 
            #     adjacent_piece.color != self._color and
            #     getattr(adjacent_piece, '_Pawn__en_passant_vulnerable', False)):
            #     return True
            
        return False

    def getNumber(self):
        return self.__number