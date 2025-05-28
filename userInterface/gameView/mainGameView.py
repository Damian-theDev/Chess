import pygame
pygame.init()

# --- screen setup ---
screen_width, screen_height = 800, 800
game_window = pygame.display.set_mode((screen_width, screen_height))

# --- peices images ---
imgWhitePawn = pygame.image.load('white-pawn.png')
imgWhiteRook = pygame.image.load('white-rook.png')
imgWhiteKnight = pygame.image.load('white-knight.png')
imgWhiteBishop = pygame.image.load('white-bishop.png')
imgWhiteQueen = pygame.image.load('white-queen.png')
imgWhiteKing = pygame.image.load('white-king.png')

imgBlackPawn = pygame.image.load('black-pawn.png')
imgBlackRook = pygame.image.load('black-rook.png')
imgBlackKnight = pygame.image.load('black-knight.png')
imgBlackBishop = pygame.image.load('black-bishop.png')
imgBlackQueen = pygame.image.load('black-queen.png')
imgBlackKing = pygame.image.load('black-king.png')

# --- game loop ---
condition = True
while condition:
    # --- draw the grid ---
    for i in range(7):
        pygame.draw.line(game_window, (255,255,255), (0, 100 + 100*i), (800, 100 + 100*i), 3)
        pygame.draw.line(game_window, (255,255,255), (100 + 100*i, 0), (100 + 100*i, 800), 3)
    pygame.display.flip()
    
    # --- exit from the game ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()