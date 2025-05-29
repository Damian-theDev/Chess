import pygame
import os
from logic import pieces, b
pygame.init()

# --- screen setup ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
gameWindow.fill((150, 80, 50))

# --- variables for the images ---
DEFAULT_PIECE_SIZE = (80, 80)
DEFAULT_PIECE_OFFSET = 10
dirImages = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')

# --- loading the pieces images ---
# --- WHITE ---
imgWhitePawn = pygame.image.load(dirImages+'\\white-pawn.png').convert_alpha(gameWindow)
imgWhitePawn = pygame.transform.scale(imgWhitePawn, DEFAULT_PIECE_SIZE)

imgWhiteRook = pygame.image.load(dirImages+'\\white-rook.png').convert_alpha(gameWindow)
imgWhiteRook = pygame.transform.scale(imgWhiteRook, DEFAULT_PIECE_SIZE)

imgWhiteKnight = pygame.image.load(dirImages+'\\white-knight.png').convert_alpha(gameWindow)
imgWhiteKnight = pygame.transform.scale(imgWhiteKnight, DEFAULT_PIECE_SIZE)

imgWhiteBishop = pygame.image.load(dirImages+'\\white-bishop.png').convert_alpha(gameWindow)
imgWhiteBishop = pygame.transform.scale(imgWhiteBishop, DEFAULT_PIECE_SIZE)

imgWhiteQueen = pygame.image.load(dirImages+'\\white-queen.png').convert_alpha(gameWindow)
imgWhiteQueen = pygame.transform.scale(imgWhiteQueen, DEFAULT_PIECE_SIZE)

imgWhiteKing = pygame.image.load(dirImages+'\\white-king.png').convert_alpha(gameWindow)
imgWhiteKing = pygame.transform.scale(imgWhiteKing, DEFAULT_PIECE_SIZE)

# --- BLACK ---
imgBlackPawn = pygame.image.load(dirImages+'\\black-pawn.png').convert_alpha(gameWindow)
imgBlackPawn = pygame.transform.scale(imgBlackPawn, DEFAULT_PIECE_SIZE)

imgBlackRook = pygame.image.load(dirImages+'\\black-rook.png').convert_alpha(gameWindow)
imgBlackRook = pygame.transform.scale(imgBlackRook, DEFAULT_PIECE_SIZE)

imgBlackKnight = pygame.image.load(dirImages+'\\black-knight.png').convert_alpha(gameWindow)
imgBlackKnight = pygame.transform.scale(imgBlackKnight, DEFAULT_PIECE_SIZE)

imgBlackBishop = pygame.image.load(dirImages+'\\black-bishop.png').convert_alpha(gameWindow)
imgBlackBishop = pygame.transform.scale(imgBlackBishop, DEFAULT_PIECE_SIZE)

imgBlackQueen = pygame.image.load(dirImages+'\\black-queen.png').convert_alpha(gameWindow)
imgBlackQueen = pygame.transform.scale(imgBlackQueen, DEFAULT_PIECE_SIZE)

imgBlackKing = pygame.image.load(dirImages+'\\black-king.png').convert_alpha(gameWindow)
imgBlackKing = pygame.transform.scale(imgBlackKing, DEFAULT_PIECE_SIZE)

# --- showing the pieces images ---
# TODO: actually link the images to the logic
gameWindow.blit(imgBlackRook, (0 + DEFAULT_PIECE_OFFSET, 0 + DEFAULT_PIECE_OFFSET))
gameWindow.blit(imgBlackRook, (700 + DEFAULT_PIECE_OFFSET, 0 + DEFAULT_PIECE_OFFSET))
gameWindow.blit(imgWhiteRook, (0 + DEFAULT_PIECE_OFFSET, 700 + DEFAULT_PIECE_OFFSET))
gameWindow.blit(imgWhiteRook, (700 + DEFAULT_PIECE_OFFSET, 700 + DEFAULT_PIECE_OFFSET))

# --- game loop ---
condition = True
while condition:
    # --- draw the grid ---
    for i in range(7):
        pygame.draw.line(gameWindow, (255,255,255), (0, 100 + 100*i), (800, 100 + 100*i), 3)
        pygame.draw.line(gameWindow, (255,255,255), (100 + 100*i, 0), (100 + 100*i, 800), 3)
    pygame.display.flip()

    # --- pygame events handling ---
    for event in pygame.event.get():
        # --- mapping mouse inputs ---
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseClickPosition = pygame.mouse.get_pos()
            
            xMouseClick, yMouseClick = (mouseClickPosition[0] // 100, mouseClickPosition[1] // 100)
            print(b.getBoard((xMouseClick, yMouseClick)))
    
    
        # --- exit from the game ---
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()