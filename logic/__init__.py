from .board import Board
from .pieces import Pawn, Queen, Rook, Knight, Bishop, King

pieces = {
    'black': {
        'pawns': [Pawn("black", i) for i in range(8)],
        'rooks': [Rook("black", 0), Rook("black", 1)],
        'knights': [Knight("black", 0), Knight("black", 1)],
        'bishops': [Bishop("black", 0), Bishop("black", 1)],
        'queen': Queen("black"),
        'king': King("black")
    },
    'white': {
        'pawns': [Pawn("white", i) for i in range(8)],
        'rooks': [Rook("white", 0), Rook("white", 1)],
        'knights': [Knight("white", 0), Knight("white", 1)],
        'bishops': [Bishop("white", 0), Bishop("white", 1)],
        'queen': Queen("white"),
        'king': King("white")
    }
}

boardStatus = [[None for _ in range(8)] for _ in range(8)]
# Black pieces (top rows)
boardStatus[0] = [
    pieces['black']['rooks'][0],
    pieces['black']['knights'][0],
    pieces['black']['bishops'][0],
    pieces['black']['queen'],
    pieces['black']['king'],
    pieces['black']['bishops'][1],
    pieces['black']['knights'][1],
    pieces['black']['rooks'][1]
]
boardStatus[1] = pieces['black']['pawns']

# White pieces (bottom rows)
boardStatus[6] = pieces['white']['pawns']
boardStatus[7] = [
    pieces['white']['rooks'][0],
    pieces['white']['knights'][0],
    pieces['white']['bishops'][0],
    pieces['white']['queen'],
    pieces['white']['king'],
    pieces['white']['bishops'][1],
    pieces['white']['knights'][1],
    pieces['white']['rooks'][1]
]

# --- initialising the board ---
board = Board()
board.setBoard(boardStatus)

for I in board.getBoard():
    s= []
    for i in I:
        if i != None:
            if i.type == 'pawn':
                s.append(f'{i.color} {i.type} {i.getNumber()}')            
            else: 
                s.append(f'{i.color} {i.type}')
        else:
            s.append(None)    
    print(s)
    
    
board.print_board_debug()