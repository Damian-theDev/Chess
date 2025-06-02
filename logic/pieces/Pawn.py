from .Piece import Piece

class Pawn(Piece):
    def __init__(self, color, number):
        startingPosition = self.__getStartingPosition(color, number)
        self.__number = number
        self.__firstMove = True

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
        oldCol, oldRow = self._currentPosition
        direction = -1 if self._color == "white" else 1  # White moves up, black moves down
        
        # --- Basic movement rules ---
        # Forward one square
        if (newCol == oldCol and 
            newRow == oldRow + direction and 
            boardState[newRow][newCol] is None):
            self.__firstMove = False
            self._currentPosition = (newCol, newRow)
            print(f'move approved ({self})') 
            return True
            
        # Forward two squares from starting position
        if (self.__firstMove and 
            newCol == oldCol and 
            newRow == oldRow + 2*direction and 
            boardState[oldRow + direction][oldCol] is None and 
            boardState[newRow][newCol] is None):
            self.__firstMove = False
            self._currentPosition = (newCol, newRow)
            print(f'move approved ({self})') 
            return True
        
        if self.attack(newRow, newCol, boardState):
            return True
        
        print(f'movent not permitted ({self})')
        return False
            
    # --- Capture rules (diagonal) ---
    def attack(self, newRow, newCol, boardState):
        oldCol, oldRow = self._currentPosition
        direction = -1 if self._color == "white" else 1  # White moves up, black moves down
        
        if (abs(newCol - oldCol) == 1 and 
            newRow == oldRow + direction and 
            boardState[newRow][newCol] is not None and 
            boardState[newRow][newCol].color != self._color):
            self.__firstMove = False
            self._currentPosition = (newCol, newRow)
            print(f'move approved ({self})') 
            return True
            
        # TODO: Implement en passant capture
        