from sys import exit

import pygame
from pygame.locals import *  # noqa
from random import randint

pygame.init()
pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - Trace Route.mp3')  # noqa
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_cape_rise.wav')

larg = 640
alt = 480

x = int(larg/2)
y = int(alt/2)

x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption('FabiGame_SoundTrack: BoxCat Games - Trace Route')
relogio = pygame.time.Clock()

while True:
    relogio.tick(100)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:  # noqa
            pygame.quit()
            exit()
        """if event.type == KEYDOWN:   # noqa
            if event.key == K_a:    # noqa
                x = x - 20
            if event.key == K_d:   # noqa
                x = x + 20
            if event.key == K_w:    # noqa
                y = y - 20
            if event.key == K_s:    # noqa
                y = y + 20"""
    
    if pygame.key.get_pressed()[K_a]:    # noqa
        x = x - 20
    if pygame.key.get_pressed()[K_d]:    # noqa
        x = x + 20
    if pygame.key.get_pressed()[K_w]:    # noqa
        y = y - 20
    if pygame.key.get_pressed()[K_s]:    # noqa
        y = y + 20   
        
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50)) # noqa
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))
    
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos = pontos + 1
        barulho_colisao.play()
    
    tela.blit(texto_formatado, (430, 30))
    pygame.display.update()


"""SoundTrack: Trace Route
BoxCat Games"""