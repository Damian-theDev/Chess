class Piece:
    def __init__(self, color, type, currentPosition, value):
        # * Base class for all chess pieces
        # Args:
        #     color (str): either 'white' or 'black'
        #     type (str): type of the piece (ex. 'pawn' or 'bihsop' exc.)
        #     currentPosition (tuple): (x, y) coordinates on the board
        #     value (int): piece's relative value
        #     statusAlive (bool): flag to check if the piece has been taken
        
        self._color = color
        self._type = type
        self._currentPosition = currentPosition
        self._value = value
        self._alive = True
        self._firstMove = True

    def __str__(self):
        return f"Generic {self._color} piece at position {self._currentPosition}"

    # --- properties definitions ---
    @property
    def color(self):
        return self._color

    @property
    def firstMove(self):
        return self._firstMove
    
    @property
    def type(self):
        return self._type

    @property
    def currentPosition(self):
        return self._currentPosition

    @currentPosition.setter
    def currentPosition(self, new_position):
        self._currentPosition = new_position

    @property
    def value(self):
        return self._value

    @property
    def alive(self):
        return self._alive

    # mark the piece as captured
    def capture(self):
        self._alive = False
        self._currentPosition = None