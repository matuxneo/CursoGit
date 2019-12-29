#!/usr/bin/python

import pygame

pygame.init()
largura = (300,200)

janela = pygame.display.set_mode(largura)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    
    janela.fill((0,255,0))
    
    pygame.draw.polygon(janela,(255,255,0),((75,100),(150,50),(225,100),(150,150)))
    pygame.draw.circle(janela,(0,0,255),(150,100),20)
    pygame.draw.line(janela,(255,255,255),(130,100),(170,100))
    
    pygame.display.flip()
