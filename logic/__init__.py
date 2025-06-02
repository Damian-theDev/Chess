from .board import Board
from .pieces import Pawn, Queen, Rook, Knight, Bishop, King

# --- initialising the board ---
b = Board()

# --- --- BLACK PEICES --- ---
# --- black royalty ---
bq = Queen("black")
b.addPiece(bq, bq.currentPosition)
bk = King("black")
b.addPiece(bk, bk.currentPosition)

# --- black rooks ---
br0 = Rook("black", 0)
b.addPiece(br0, br0.currentPosition)
br1 = Rook("black", 1)
b.addPiece(br1, br1.currentPosition)

# --- black knights ---
bn0 = Knight("black", 0)
b.addPiece(bn0, bn0.currentPosition)
bn1 = Knight("black", 1)
b.addPiece(bn1, bn1.currentPosition)

# --- black bishops ---
bb0 = Bishop("black", 0)
b.addPiece(bb0, bb0.currentPosition)
bb1 = Bishop("black", 1)
b.addPiece(bb1, bb1.currentPosition)

# --- black pawns ---
bp0 = Pawn("black", 0)
b.addPiece(bp0, bp0.currentPosition)
bp1 = Pawn("black", 1)
b.addPiece(bp1, bp1.currentPosition)
bp2 = Pawn("black", 2)
b.addPiece(bp2, bp2.currentPosition)
bp3 = Pawn("black", 3)
b.addPiece(bp3, bp3.currentPosition)
bp4 = Pawn("black", 4)
b.addPiece(bp4, bp4.currentPosition)
bp5 = Pawn("black", 5)
b.addPiece(bp5, bp5.currentPosition)
bp6 = Pawn("black", 6)
b.addPiece(bp6, bp6.currentPosition)
bp7 = Pawn("black", 7)
b.addPiece(bp7, bp7.currentPosition)

# --- --- WHITE PEICES --- ---
# --- white royalty --- 
wq = Queen("white")
b.addPiece(wq, wq.currentPosition)
wk = King("white")
b.addPiece(wk, wk.currentPosition)

# --- white rooks ---
wr0 = Rook("white", 0)
b.addPiece(wr0, wr0.currentPosition)
wr1 = Rook("white", 1)
b.addPiece(wr1, wr1.currentPosition)

# --- white knights ---
wn0 = Knight("white", 0)
b.addPiece(wn0, wn0.currentPosition)
wn1 = Knight("white", 1)
b.addPiece(wn1, wn1.currentPosition)

# --- white bishops ---
wb0 = Bishop("white", 0)
b.addPiece(wb0, wb0.currentPosition)
wb1 = Bishop("white", 1)
b.addPiece(wb1, wb1.currentPosition)

# --- white pawns ---
wp0 = Pawn("white", 0)
b.addPiece(wp0, wp0.currentPosition)
wp1 = Pawn("white", 1)
b.addPiece(wp1, wp1.currentPosition)
wp2 = Pawn("white", 2)
b.addPiece(wp2, wp2.currentPosition)
wp3 = Pawn("white", 3)
b.addPiece(wp3, wp3.currentPosition)
wp4 = Pawn("white", 4)
b.addPiece(wp4, wp4.currentPosition)
wp5 = Pawn("white", 5)
b.addPiece(wp5, wp5.currentPosition)
wp6 = Pawn("white", 6)
b.addPiece(wp6, wp6.currentPosition)
wp7 = Pawn("white", 7)
b.addPiece(wp7, wp7.currentPosition)

pieces = {
    'black': {
        'pawnArray': [bp0, bp1, bp2, bp3, bp4, bp5, bp6, bp7],
        'rookArray': [br0, br1],
        'knightArray': [bn0, bn1],
        'bishopArray': [bb0, bb1],
        'queen': bq,
        'king': bk
    },
        'white': {
        'pawnArray': [wp0, wp1, wp2, wp3, wp4, wp5, wp6, wp7],
        'rookArray': [wr0, wr1],
        'knightArray': [wn0, wn1],
        'bishopArray': [wb0, wb1],
        'queen': wq,
        'king': wk
    },
}