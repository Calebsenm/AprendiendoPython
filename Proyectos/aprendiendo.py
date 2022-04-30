#crea el primer elemento de la ventana
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
 
    pygame.display.update()
