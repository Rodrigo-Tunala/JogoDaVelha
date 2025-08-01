import pygame
pygame.init()

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] ==jogador:
            return True

    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if '' in linha:
            return False
        
    return True
import random

def jogada_ia(tabuleiro):
    pygame.time.delay(500)
    pygame.event.clear()
    # Ver se a IA pode vencer em uma jogada
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == '':
                tabuleiro[linha][coluna] = 'O'
                if verificar_vitoria(tabuleiro, 'O'):
                    return
                tabuleiro[linha][coluna] = ''

    # Ver se o jogador pode vencer e bloquear
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == '':
                tabuleiro[linha][coluna] = 'X'
                if verificar_vitoria(tabuleiro, 'X'):
                    tabuleiro[linha][coluna] = 'O'
                    return
                tabuleiro[linha][coluna] = ''

    # Caso contrário, jogar na primeira posição livre
    posicoes_vazias = []
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == '':
                posicoes_vazias.append((linha, coluna))
    if posicoes_vazias:
        linha_escolhida, coluna_escolhida = random.choice(posicoes_vazias)
        tabuleiro[linha_escolhida][coluna_escolhida] = 'O'
            
def menu_inicial():
    
    fonte_titulo = pygame.font.Font(None, 60)
    fonte_botao = pygame.font.Font(None,50)

    while True:
        tela.fill((preto))


        titulo = fonte_titulo.render('Escolha o modo de jogo', True, branco)
        tela.blit(titulo, (70,100))

        botao_pve = pygame.Rect(150, 250, 300, 60)
        pygame.draw.rect(tela, branco, botao_pve, border_radius=10)
        texto_pve = fonte_botao.render('1 Jogador', True, (0, 0, 0))
        tela.blit(texto_pve, (botao_pve.x + 70, botao_pve.y + 10))
        
        botao_pvp = pygame.Rect(150, 350, 300, 60)
        pygame.draw.rect(tela, branco, botao_pvp, border_radius=10)
        texto_pvp = fonte_botao.render('2 Jogadores', True , (0, 0, 0))
        tela.blit(texto_pvp, (botao_pvp.x + 40, botao_pvp.y +10))


        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if botao_pvp.collidepoint(x, y):
                    return 'PvP'
                    
                elif botao_pve.collidepoint(x, y):
                    return 'PvE'

def desenhar_tabuleiro():
    tela.fill((preto))
    pygame.draw.line(tela, branco, (0, 200), (600, 200), 5)
    pygame.draw.line(tela, branco, (0, 400), (600, 400), 5)
    pygame.draw.line(tela, branco, (200, 0), (200, 600), 5)
    pygame.draw.line(tela, branco, (400, 0), (400, 600), 5)
    for linha in range(3):
        for coluna in range(3):
            posicao = tabuleiro[linha][coluna]
            if posicao != '':
                imagem = fonte.render(posicao, True, branco)
                X = (coluna * 200) + 100
                Y = (linha * 200) + 100
                centro = imagem.get_rect(center=(X, Y))
                tela.blit(imagem, centro)
    texto_placar = fonte_placar.render(f'X: {jogador_x} O: {jogador_o} E: {empate}', True, branco)
    tela.blit(texto_placar, (10, 10))
    pygame.display.update() 

tamanho = (600, 600)
branco = (255, 255, 255)
preto = (0, 0, 0)

tela = pygame.display.set_mode(tamanho)


pygame.display.set_caption('Jogo da Velha')

tabuleiro = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
linha = 0
coluna = 0
jogador_atual = 'X'
modo_jogo = menu_inicial()


jogador_x = 0
jogador_o = 0
empate = 0

rodando = True

fonte = pygame.font.Font(None, 150)
fonte_placar = pygame.font.Font(None, 40)


menu_inicial()

while rodando:
    

    desenhar_tabuleiro()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicao = pygame.mouse.get_pos()
            x, y = posicao
            coluna = x // 200
            linha = y // 200
            print(f'Clicou na linha {linha + 1}, coluna {coluna + 1}')
            


            if tabuleiro[linha][coluna] == '':
                tabuleiro[linha][coluna] = jogador_atual


                if verificar_vitoria(tabuleiro, jogador_atual):
                    
                    print(F'O Jogador {jogador_atual} Venceu.')
                    
                    desenhar_tabuleiro()
    
                    
                    if jogador_atual == 'X':
                        jogador_x += 1
                    else:
                        jogador_o+= 1

                    pygame.time.delay(2000)
                    pygame.event.clear()
                    tabuleiro = [
                        ['', '', ''],
                        ['', '', ''],
                        ['', '', '']
                    ]
                    jogador_atual = 'X'
                    continue

                if verificar_empate(tabuleiro):   
                    
                    desenhar_tabuleiro()

                    empate += 1 

                            
                    pygame.time.delay(2000)
                    pygame.event.clear()
                    tabuleiro = [
                        ['', '', ''],
                        ['', '', ''],
                        ['', '', '']
                    ]
                    jogador_atual = 'X'
                    continue

                if modo_jogo == 'PvP':
                    if jogador_atual == 'X':
                        jogador_atual = 'O'
                    else:
                        jogador_atual = 'X'


                    
                    


                if modo_jogo == 'PvE':
                    if jogador_atual == 'X':
                        

                        
                        # Jogada da IA após a vez do jogador
                    
                        desenhar_tabuleiro()
                        jogada_ia(tabuleiro)
                        desenhar_tabuleiro()
                        
                        if verificar_vitoria(tabuleiro, 'O'):
                            desenhar_tabuleiro()
                            print('O Jogador O Venceu.')
                            jogador_o += 1
                            pygame.time.delay(2000)
                            pygame.event.clear()
                            tabuleiro = [['', '', ''],
                                         ['', '', ''],
                                         ['', '','']]
                                   
                            jogador_atual = 'X'                            
                            continue

                        if verificar_empate(tabuleiro):
                            desenhar_tabuleiro()
                            empate += 1
                            pygame.time.delay(2000)
                            pygame.event.clear()
                            tabuleiro = [['', '', ''],
                                         ['', '', ''],
                                         ['', '', '']]
                            jogador_atual = 'X'
                            continue
                                
                        jogador_atual = 'X'
                print(tabuleiro)

pygame.quit()