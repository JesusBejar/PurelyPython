import pygame

# PARA INICIALIZAR PYGAME
pygame.init()

# PARA CREAR LA PANTALLA
# dentro de .set_mode determinas ancho y alto
# primer numero = alto, segundo numero = ancho
pantalla = pygame.display.set_mode((800, 600))

#TITULO & ICONO
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# LOOP DEL JUEGO
se_ejecuta = True 
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
