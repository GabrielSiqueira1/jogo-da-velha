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

grid = carregar_img('img/grid.png', [COMPRIMENTO_JANELA, COMPRIMENTO_JANELA])
ICON_X = carregar_img('img/1.png', [COMPRIMENTO_JANELA//3 , COMPRIMENTO_JANELA//3])
ICON_O = carregar_img('img/0.png', [COMPRIMENTO_JANELA//3, COMPRIMENTO_JANELA//3])
JOGADOR_1 = 0
JOGADOR_2 = 1
jogador = JOGADOR_1
tabuleiro = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]
    
def turno(jogador_atual):
    coordenada_atual = pygame.math.Vector2(pygame.mouse.get_pos()) // (COMPRIMENTO_JANELA // 3)
    if pygame.mouse.get_pressed()[0]:
        coluna, linha = map(int, coordenada_atual)
        tabuleiro[linha][coluna] = 0 if jogador_atual == 0 else 1
        jogador_atual = 1 - jogador_atual
        
    return jogador_atual
    
def carregar_icones():
    for i, linha in enumerate(tabuleiro):
        for j, coluna in enumerate(tabuleiro[i]):
            if tabuleiro[i][j] == 0:
                screen.blit(ICON_O, (j * (COMPRIMENTO_JANELA // 3), i * (COMPRIMENTO_JANELA // 3)))
            if tabuleiro[i][j] == 1:
                screen.blit(ICON_X, (j * (COMPRIMENTO_JANELA // 3), i * (COMPRIMENTO_JANELA // 3)))
                
def tem_icones_iguais(icones, jogador_do_jogo):
    for icone in enumerate(icones):
        if icone != jogador_do_jogo:
            return False
    return True

def tem_vencedor_linha(jogador_do_jogo):
    return tem_icones_iguais(tabuleiro[0], jogador_do_jogo)\
        or tem_icones_iguais(tabuleiro[1], jogador_do_jogo)\
        or tem_icones_iguais(tabuleiro[2], jogador_do_jogo)

def tem_vencedor_coluna(jogador_do_jogo):
    return tem_icones_iguais([tabuleiro[0][0], tabuleiro[1][0], tabuleiro[2][0]], jogador_do_jogo)\
        or tem_icones_iguais([tabuleiro[0][1], tabuleiro[1][1], tabuleiro[2][1]], jogador_do_jogo)\
        or tem_icones_iguais([tabuleiro[0][2], tabuleiro[1][2], tabuleiro[2][2]], jogador_do_jogo)
        
def tem_vencedor_diagonal(jogador_do_jogo):
    return tem_icones_iguais([tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]], jogador_do_jogo)\
        or tem_icones_iguais([tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]], jogador_do_jogo)
                
def e_vencedor(jogador_do_jogo):
    return tem_vencedor_linha(jogador_do_jogo)\
        or tem_vencedor_coluna(jogador_do_jogo)\
        or tem_vencedor_diagonal(jogador_do_jogo)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False
            
    # RENDER YOUR GAME HERE

    # fill the screen with a color to wipe away anything from last frame
    # flip() the display to put your work on screen
    pygame.display.flip()
    screen.fill("white")
    screen.blit(grid, (0, 0))
    jogador = turno(jogador)
    carregar_icones()
    pygame.event.wait()

    clock.tick(60)  # limits FPS to 60

pygame.quit()