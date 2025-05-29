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

# --- Load all chess piece images ---
def loadPieceImages():
    # --- Load white pieces ---
    pieceImages['white']['pawn'] = pygame.transform.scale(
        pygame.image.load(os.path.join(dirImages, 'white-pawn.png')).convert_alpha(gameWindow),
        DEFAULT_PIECE_SIZE
    )
    pieceImages['white']['rook'] = pygame.transform.scale(
        pygame.image.load(os.path.join(dirImages, 'white-rook.png')).convert_alpha(gameWindow),
        DEFAULT_PIECE_SIZE
    )
    pieceImages['white']['knight'] = pygame.transform.scale(
        pygame.image.load(os.path.join(dirImages, 'white-knight.png')).convert_alpha(gameWindow),
        DEFAULT_PIECE_SIZE
    )
    pieceImages['white']['bishop'] = pygame.transform.scale(
        pygame.image.load(os.path.join(dirImages, 'white-bishop.png')).convert_alpha(gameWindow),
        DEFAULT_PIECE_SIZE
    )
    pieceImages['white']['queen'] = pygame.transform.scale(
        pygame.image.load(os.path.join(dirImages, 'white-queen.png')).convert_alpha(gameWindow),
        DEFAULT_PIECE_SIZE
    )
    pieceImages['white']['king'] = pygame.transform.scale(
        pygame.image.load(os.path.join(dirImages, 'white-king.png')).convert_alpha(gameWindow),
        DEFAULT_PIECE_SIZE
    )
    
    # --- Load black pieces ---
    pieceImages['black']['pawn'] = pygame.transform.scale(
        pygame.image.load(os.path.join(dirImages, 'black-pawn.png')).convert_alpha(gameWindow),
        DEFAULT_PIECE_SIZE
    )
    pieceImages['black']['rook'] = pygame.transform.scale(
        pygame.image.load(os.path.join(dirImages, 'black-rook.png')).convert_alpha(gameWindow),
        DEFAULT_PIECE_SIZE
    )
    pieceImages['black']['knight'] = pygame.transform.scale(
        pygame.image.load(os.path.join(dirImages, 'black-knight.png')).convert_alpha(gameWindow),
        DEFAULT_PIECE_SIZE
    )
    pieceImages['black']['bishop'] = pygame.transform.scale(
        pygame.image.load(os.path.join(dirImages, 'black-bishop.png')).convert_alpha(gameWindow),
        DEFAULT_PIECE_SIZE
    )
    pieceImages['black']['queen'] = pygame.transform.scale(
        pygame.image.load(os.path.join(dirImages, 'black-queen.png')).convert_alpha(gameWindow),
        DEFAULT_PIECE_SIZE
    )
    pieceImages['black']['king'] = pygame.transform.scale(
        pygame.image.load(os.path.join(dirImages, 'black-king.png')).convert_alpha(gameWindow),
        DEFAULT_PIECE_SIZE
    )

# --- Call the function to load images ---
loadPieceImages()

# --- Game state variables ---
selectedPiece = None  # Currently selected piece (row, col)
isDragging = False  # Flag for when piece is being dragged
dragOffset = (0, 0)  # Offset between mouse and piece top-left corner

#TODO link the board directly
# --- Initial board setup ---
boardState = [
    ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight', 'black_rook'],
    ['black_pawn'] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    ['white_pawn'] * 8,
    ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight', 'white_rook']
]

# --- Draw the chess board ---
def drawBoard():
    # --- Draw alternating squares ---
    for row in range(8):
        for col in range(8):
            # Light squares for even sum, dark for odd
            squareColor = (210, 180, 140) if (row + col) % 2 == 0 else (100, 60, 30)
            pygame.draw.rect(gameWindow, squareColor, (col * 100, row * 100, 100, 100))
    
    # --- Draw grid lines ---
    for i in range(7):
        pygame.draw.line(gameWindow, (255, 255, 255), (0, 100 + 100*i), (800, 100 + 100*i), 3)
        pygame.draw.line(gameWindow, (255, 255, 255), (100 + 100*i, 0), (100 + 100*i, 800), 3)

# --- Draw all chess pieces ---
def drawPieces():
    # --- Draw all pieces except the one being dragged ---
    for row in range(8):
        for col in range(8):
            piece = boardState[row][col]
            if piece and (not isDragging or (row, col) != selectedPiece):
                color, pieceType = piece.split('_')
                img = pieceImages[color][pieceType]
                gameWindow.blit(img, (col * 100 + DEFAULT_PIECE_OFFSET, row * 100 + DEFAULT_PIECE_OFFSET))
    
    # --- Draw the dragged piece on top ---
    if isDragging and selectedPiece:
        row, col = selectedPiece
        piece = boardState[row][col]
        if piece:
            color, pieceType = piece.split('_')
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
    pygame.display.flip()  # Update the display

    # --- Handle events ---
    for event in pygame.event.get():
        # --- Exit the game ---
        if event.type == pygame.QUIT:
            isRunning = False
        
        # --- Mouse button down (select piece) ---
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouseX, mouseY = event.pos
                col, row = mouseX // 100, mouseY // 100
                
                # --- Check if clicked on a piece ---
                if 0 <= row < 8 and 0 <= col < 8 and boardState[row][col]:
                    selectedPiece = (row, col)
                    isDragging = True
                    # --- Calculate offset from piece corner ---
                    dragOffset = (mouseX - col * 100, mouseY - row * 100)
        
        # --- Mouse button up (drop piece) ---
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and isDragging:  # Left mouse button
                mouseX, mouseY = event.pos
                newCol, newRow = mouseX // 100, mouseY // 100
                
                # --- Validate move (TODO: replace with actual chess logic) ---
                if (0 <= newRow < 8 and 0 <= newCol < 8 and 
                    (newRow, newCol) != selectedPiece):
                    
                    # --- Move the piece ---
                    piece = boardState[selectedPiece[0]][selectedPiece[1]]
                    boardState[selectedPiece[0]][selectedPiece[1]] = None
                    boardState[newRow][newCol] = piece
                
                # --- Reset dragging state ---
                isDragging = False
                selectedPiece = None
        
        # --- Mouse motion (dragging piece) ---
        elif event.type == pygame.MOUSEMOTION and isDragging:
            pass  # Handled in drawPieces()

# --- Clean up ---
pygame.quit()