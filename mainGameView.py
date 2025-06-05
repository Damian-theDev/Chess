import pygame
import os
from logic import board

# --- Initialize pygame ---
pygame.init()

# --- Screen setup ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 830
gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
gameWindow.fill((150, 80, 50))  # Fill with brown background

# --- Variables for the images ---
IMG_OFFSET = 10
dirImages = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')

# --- Piece positioning constants ---
SQUARE_SIZE = 100
PIECE_SIZE = 80
PIECE_OFFSET = (SQUARE_SIZE - PIECE_SIZE) // 2  # Centers piece in square (10px)
INDICATOR_HEIGHT = 30

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
        pieceImages[color][piece] = pygame.transform.scale(img, (PIECE_SIZE, PIECE_SIZE))

# --- game state variables ---
selectedPiece = None    # currently selected piece (row, col)
isDragging = False      # flag: is the player dragging something
dragOffset = (0, 0)     # offset between mouse and piece top-left corner

# --- draw the chess board underneath ---
def drawBoard():
    # --- alternating squares ---
    for row in range(8):
        for col in range(8):
            # using light squares for even sum, dark for odd
            squareColor = (210, 180, 140) if (row + col) % 2 == 0 else (100, 60, 30)
            pygame.draw.rect(gameWindow, squareColor, 
                           (col * SQUARE_SIZE, 
                            row * SQUARE_SIZE + INDICATOR_HEIGHT,
                            SQUARE_SIZE, SQUARE_SIZE))
    
    # --- grid lines ---
    for i in range(9):
        # Horizontal lines
        pygame.draw.line(gameWindow, (255, 255, 255),
                        (0, i * SQUARE_SIZE + INDICATOR_HEIGHT),
                        (SCREEN_WIDTH, i * SQUARE_SIZE + INDICATOR_HEIGHT), 3)
        # Vertical lines
        pygame.draw.line(gameWindow, (255, 255, 255),
                        (i * SQUARE_SIZE, INDICATOR_HEIGHT),
                        (i * SQUARE_SIZE, SCREEN_HEIGHT), 3)

# --- draw all chess pieces ---
def drawPieces():
    # --- draw all pieces, except the one being dragged ---
    for row in range(8):
        for col in range(8):
            piece = board.getBoard()[row][col]
            if piece and (not isDragging or (row, col) != selectedPiece):
                img = pieceImages[piece.color][piece.type]
                gameWindow.blit(img, 
                              (col * SQUARE_SIZE + PIECE_OFFSET,
                               row * SQUARE_SIZE + PIECE_OFFSET + INDICATOR_HEIGHT))
    
def drawDraggedPiece():
    # --- draw the dragged piece on top ---
    if isDragging and selectedPiece:
        piece = board.getBoard()[selectedPiece[0]][selectedPiece[1]]
        if piece:
            img = pieceImages[piece.color][piece.type]
            mouseX, mouseY = pygame.mouse.get_pos()
            # center the img on mouse cursor
            gameWindow.blit(img, (mouseX - PIECE_SIZE/2, mouseY - INDICATOR_HEIGHT))
            
def drawTurnIndicator(gameOver, currentTurn, winner):
    # text setup
    font = pygame.font.SysFont('Arial', 24)
    text = f"Game Over! {winner} wins!" if gameOver else f"{currentTurn}'s turn"
    textSurface = font.render(text, True, (255, 255, 255))
    
    # indicator background
    pygame.draw.rect(gameWindow, (50, 50, 50), 
                   (0, 0, SCREEN_WIDTH, INDICATOR_HEIGHT))
    
    # centered text
    text_rect = textSurface.get_rect(center=(SCREEN_WIDTH//2, INDICATOR_HEIGHT//2))
    gameWindow.blit(textSurface, text_rect)

def getBoardPositionFromMouse(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = (y - INDICATOR_HEIGHT) // SQUARE_SIZE
    return (row, col) if 0 <= row < 8 and 0 <= col < 8 else (None, None)

# --- Main game loop ---
isRunning = True
gameOver = False
currentTurn = 'white'
winner = None

while isRunning:
    # --- clear and redraw everything ---
    gameWindow.fill((150, 80, 50))
    drawBoard()
    drawPieces()
    drawDraggedPiece()
    drawTurnIndicator(gameOver, currentTurn, winner)
    pygame.display.flip()  # Update the display

    # --- events handler ---
    for event in pygame.event.get():
        # --- exit the game ---
        if event.type == pygame.QUIT:
            isRunning = False
        
        # --- mouse button down (select piece) ---
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not gameOver:
                row, col = getBoardPositionFromMouse(event.pos)
                # --- check if the player clicked one of thier pieces ---
                if row is not None and board.getBoard()[row][col] and board.getBoard()[row][col].color == currentTurn:
                    selectedPiece = (row, col)
                    isDragging = True
                    # --- calculate offset from piece center ---
                    mouseX, mouseY = event.pos
                    dragOffset = (mouseX - (col * SQUARE_SIZE + PIECE_OFFSET),
                                mouseY - (row * SQUARE_SIZE + PIECE_OFFSET + INDICATOR_HEIGHT))
        
        # --- mouse button up (drop piece) ---
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and isDragging and not gameOver:
                mouseX, mouseY = event.pos
                newCol, newRow = (mouseX) // 100, (mouseY - INDICATOR_HEIGHT) // 100
            
                # Validate moves and turn
                if (0 <= newRow < 8 and 0 <= newCol < 8 and 
                    (newRow, newCol) != selectedPiece):
                    
                    boardState = board.getBoard()
                    targetPiece = boardState[newRow][newCol]
                    piece = boardState[selectedPiece[0]][selectedPiece[1]]
                    
                    # only allow to move your own pieces
                    if (piece and piece.color == currentTurn and 
                        piece.validateMove(newRow, newCol, boardState)):
                        
                        # --- Handle castling ---
                        if (piece.type == 'king' and 
                            abs(newCol - selectedPiece[1]) == 2):  # Castling move
                            
                            # Determine rook position and new position
                            direction = 1 if newCol > selectedPiece[1] else -1  # 1=kingside, -1=queenside
                            rook_col = 7 if direction == 1 else 0
                            rook_new_col = newCol - direction  # Rook moves adjacent to king
                            
                            # Get and move the rook
                            rook = boardState[selectedPiece[0]][rook_col]
                         
                            if rook and rook.type == 'rook':
                                # Update rook position
                                rook._currentPosition = (selectedPiece[0], rook_new_col)
                                rook._firstMove = False
                                # Update board state
                                boardState[selectedPiece[0]][rook_col] = None
                                boardState[selectedPiece[0]][rook_new_col] = rook
                
                        # --- eventually kill the target ---
                        if targetPiece != None:
                            targetPiece._alive = False
                        
                        # --- move the piece ---
                        piece._currentPosition = (newCol, newRow)
                        if piece._firstMove:
                            piece._firstMove = False
                        boardState[selectedPiece[0]][selectedPiece[1]] = None
                        boardState[newRow][newCol] = piece

                        # --- check mate ---
                        if targetPiece and targetPiece.type == 'king':
                            gameOver = True
                            winner = currentTurn
                        
                        # --- change turn ---
                        currentTurn = 'black' if currentTurn == 'white' else 'white'
                
                        board.print_board_debug()
                            
            # --- reset dragging flags ---
            isDragging = False
            selectedPiece = None
        
        # --- mouse motion (dragging piece) ---
        elif event.type == pygame.MOUSEMOTION and isDragging:
            pass  # already handled in drawDraggedPiece()

# --- end the program ---
pygame.quit()