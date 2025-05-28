# importing all the developed classes
from logic.pieces import Queen, Pawn
from logic.board.Board import Board

b = Board()

wq = Queen("white")
bq = Queen("black")

b.addPiece(wq, "73")
b.addPiece(bq, "03")

b.printBoard()