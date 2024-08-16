from curses import KEY_LEFT
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
# variable del jugador
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0

# funcion jugador 
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))
# LOOP DEL JUEGO
se_ejecuta = True 
while se_ejecuta:
    # RGB COLOR DE FONDO
    pantalla.fill((250, 242, 7))
    # jugador_x += 0.1
     
    #  iterar eventos
    for evento in pygame.event.get():
        # evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento presionar flechas
        # KEYDOWN
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                # print("flecha izquierda")
                jugador_x_cambio = -0.5
            if evento.key == pygame.K_RIGHT:
                # print("flecha derecha")
                jugador_x_cambio = 0.5
        # evento soltar flechas
        # KEYUP
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                # print("flecha fue soltada")
                jugador_x_cambio = 0
    # modificar lugar del jugador
    jugador_x += jugador_x_cambio

    jugador(jugador_x, jugador_y)

    # actualizar
    pygame.display.update()