class Piece():
    def __init__(self, color, currentPosition, value, statusAlive):
        self.__color = color
        self.__currentPosition = currentPosition
        self.__value = value
        self.__statusAlive = statusAlive

    def __str__(self):
        return f"generic {self.__color} piece on position {self.__currentPosition}"

    def __getStartingPosition(self):
        print ("--- ERROR(Piece.__getStartingPosition): piece type was not specified (use the dedicated classes) ---")

    # def getCurrentPosition(self):
    #     print ("--- ERROR(Piece.getCurrentPosition): piece type was not specified, can not define position of a generic piece ---")
    def getCurrentPosition(self):
        return self.__currentPosition