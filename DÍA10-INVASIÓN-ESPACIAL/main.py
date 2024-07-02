import pygame

# PARA INICIALIZAR PYGAME
pygame.init()

# PARA CREAR LA PANTALLA
# dentro de .set_mode determinas ancho y alto
# primer numero = alto, segundo numero = ancho
pantalla = pygame.display.set_mode((800, 600))

#TITULO & ICONO
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("./DÍA10-INVASIÓN-ESPACIAL/ovni.png")
pygame.display.set_icon(icono)

# ICONO DE JUGADOR
img_jugador = pygame.image.load("./DÍA10-INVASIÓN-ESPACIAL/cohete.png")
jugador_x = 368
jugador_y = 536

def jugador():
    pantalla.blit(img_jugador, (jugador_x, jugador_y))
# LOOP DEL JUEGO
se_ejecuta = True 
while se_ejecuta:
    # RGB COLOR DE FONDO
    pantalla.fill((250, 242, 7))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    jugador()

    pygame.display.update()