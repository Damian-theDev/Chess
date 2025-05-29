class Piece:
    def __init__(self, color, currentPosition, value):
        # * Base class for all chess pieces
        # Args:
        #     color (str): either 'white' or 'black'
        #     currentPosition (tuple): (x, y) coordinates on the board
        #     value (int): piece's relative value
        #     statusAlive (bool): flag to check if the piece has been taken
        
        self._color = color
        self._currentPosition = currentPosition
        self._value = value
        self._statusAlive = True

    def __str__(self):
        return f"Generic {self._color} piece at position {self._currentPosition}"

    # --- properties definitions ---
    @property
    def color(self):
        return self._color

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
    def isAlive(self):
        return self._statusAlive

    # mark the piece as captured
    def capture(self):
        self._statusAlive = False
        self._currentPosition = None