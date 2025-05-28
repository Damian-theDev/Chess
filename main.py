# importing all the developed classes
from logic.pieces import Queen, Pawn
from logic.board.Board import Board

b = Board()

wq = Queen("white")
bq = Queen("black")

b.addPiece(wq, "04")
b.addPiece(bq, "74")

# --------------------

wp0 = Pawn("white", 0)

b.addPiece(wp0, "10")


b.printBoard()