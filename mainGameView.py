import pygame
import os
from logic import pieces, b

# --- Initialize pygame ---
pygame.init()

# --- Screen setup ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
gameWindow.fill((150, 80, 50))  # Fill with brown background

# --- Variables for the images ---
DEFAULT_PIECE_SIZE = (80, 80)  # Size of each chess piece
DEFAULT_PIECE_OFFSET = 10  # Offset from the square edges
dirImages = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')

# --- Dictionary to store all piece images ---
pieceImages = {
    'white': {
        'pawn': None,
        'rook': None,
        'knight': None,
        'bishop': None,
        'queen': None,
        'king': None
    },
    'black': {
        'pawn': None,
        'rook': None,
        'knight': None,
        'bishop': None,
        'queen': None,
        'king': None
    }
}

# --- load all chess piece images with a loop ---
for color in ('white', 'black'):
    for piece in ('pawn', 'rook', 'knight', 'bishop', 'queen', 'king'):
        filename = f"{color}-{piece}.png"
        path = os.path.join(dirImages, filename)
        img = pygame.image.load(path).convert_alpha(gameWindow)
        pieceImages[color][piece] = pygame.transform.scale(img, DEFAULT_PIECE_SIZE)

# --- game state variables ---
selectedPiece = None    # currently selected piece (row, col)
isDragging = False      # flag: is the player dragging something
dragOffset = (0, 0)     # offset between mouse and piece top-left corner

# --- initial board setup with linked objs ---
boardState = [
    [pieces['black']['rookArray'][0], pieces['black']['knightArray'][0], pieces['black']['bishopArray'][0], pieces['black']['queen'], pieces['black']['king'], pieces['black']['bishopArray'][1], pieces['black']['knightArray'][1], pieces['black']['rookArray'][1]],
    pieces['black']['pawnArray'],
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    pieces['white']['pawnArray'],
    [pieces['white']['rookArray'][0], pieces['white']['knightArray'][0], pieces['white']['bishopArray'][0], pieces['white']['queen'], pieces['white']['king'], pieces['white']['bishopArray'][1], pieces['white']['knightArray'][1], pieces['white']['rookArray'][1]]
]

# --- draw the chess board underneath ---
def drawBoard():
    # --- alternating squares ---
    for row in range(8):
        for col in range(8):
            # using light squares for even sum, dark for odd
            squareColor = (210, 180, 140) if (row + col) % 2 == 0 else (100, 60, 30)
            pygame.draw.rect(gameWindow, squareColor, (col * 100, row * 100, 100, 100))
    
    # --- grid lines ---
    for i in range(7):
        pygame.draw.line(gameWindow, (255, 255, 255), (0, 100 + 100*i), (800, 100 + 100*i), 3)
        pygame.draw.line(gameWindow, (255, 255, 255), (100 + 100*i, 0), (100 + 100*i, 800), 3)

# --- draw all chess pieces ---
def drawPieces():
    # --- draw all pieces, except the one being dragged ---
    for row in range(8):
        for col in range(8):
            piece = boardState[row][col]
            if piece and (not isDragging or (row, col) != selectedPiece):
                color, pieceType = piece.color, piece.type
                img = pieceImages[color][pieceType]
                gameWindow.blit(img, (col * 100 + DEFAULT_PIECE_OFFSET, row * 100 + DEFAULT_PIECE_OFFSET))
    
def drawDraggedPiece():
    # --- draw the dragged piece on top ---
    if isDragging and selectedPiece:
        row, col = selectedPiece
        piece = boardState[row][col]
        if piece:
            color, pieceType = piece.color, piece.type
            img = pieceImages[color][pieceType]
            mouseX, mouseY = pygame.mouse.get_pos()
            gameWindow.blit(img, (mouseX - dragOffset[0], mouseY - dragOffset[1]))

# --- Main game loop ---
isRunning = True
while isRunning:
    # --- Clear and redraw everything ---
    gameWindow.fill((150, 80, 50))  # Brown background
    drawBoard()
    drawPieces()
    drawDraggedPiece()
    pygame.display.flip()  # Update the display

    # --- events handler ---
    for event in pygame.event.get():
        # --- exit the game ---
        if event.type == pygame.QUIT:
            isRunning = False
        
        # --- mouse button down (select piece) ---
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:                   # Left mouse button
                mouseX, mouseY = event.pos
                col, row = mouseX // 100, mouseY // 100
                
                # --- check if a piece was clicked ---
                if 0 <= row < 8 and 0 <= col < 8 and boardState[row][col]:
                    selectedPiece = (row, col)
                    isDragging = True
                    # --- calculate the offset from piece to corner of the selected square ---
                    dragOffset = (mouseX - col * 100, mouseY - row * 100)
        
        # --- mouse button up (drop piece) ---
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and isDragging:    # left mouse button
                mouseX, mouseY = event.pos
                newCol, newRow = mouseX // 100, mouseY // 100
                
                # --- validate moves ---
                if (0 <= newRow < 8 and 0 <= newCol < 8 and 
                    (newRow, newCol) != selectedPiece):
                    
                    piece = boardState[selectedPiece[0]][selectedPiece[1]]
                    if piece.validateMove(newRow, newCol, boardState):
                        # --- move the piece ---
                        boardState[selectedPiece[0]][selectedPiece[1]] = None
                        boardState[newRow][newCol] = piece
                        
                        #TODO : add turn logic
                    
                # --- reset dragging flags ---
                isDragging = False
                selectedPiece = None
        
        # --- mouse motion (dragging piece) ---
        elif event.type == pygame.MOUSEMOTION and isDragging:
            pass  # already handled in drawDraggedPiece()

# --- end the program ---
pygame.quit()