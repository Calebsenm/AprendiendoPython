import pygame
import sys

pygame.init()

LaPantalla = pygame.display.set_mode((500,400))

pygame.display.set_caption("MI Primer Ventana :D")

while True:
    #manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #logica
    pygame.draw.rect(LaPantalla,(255,0,0),(400,400,50,50))
    pygame.display.update

   