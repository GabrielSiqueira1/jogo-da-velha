# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
COMPRIMENTO_JANELA = 720
screen = pygame.display.set_mode((COMPRIMENTO_JANELA, COMPRIMENTO_JANELA))
clock = pygame.time.Clock()
running = True

# instância das imagens

def carregar_img(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)

    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    grid = carregar_img('img/grid.png', [COMPRIMENTO_JANELA, COMPRIMENTO_JANELA])
    ICON_X = carregar_img('img/1.png', [COMPRIMENTO_JANELA//3, COMPRIMENTO_JANELA//3])
    ICON_O = carregar_img('img/0.png', [COMPRIMENTO_JANELA//3, COMPRIMENTO_JANELA//3])
    screen.blit(grid, (0, 0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()