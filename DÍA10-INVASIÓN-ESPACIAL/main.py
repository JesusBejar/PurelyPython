from curses import KEY_LEFT
import pygame
import random 

# PARA INICIALIZAR PYGAME
pygame.init()

# PARA CREAR LA PANTALLA
# dentro de .set_mode determinas ancho y alto
# primer numero = alto, segundo numero = ancho
pantalla = pygame.display.set_mode((800, 600))
fondo = pygame.image.load("./DÍA10-INVASIÓN-ESPACIAL/fondo.png")

#TITULO & ICONO
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("./DÍA10-INVASIÓN-ESPACIAL/ovni.png")
pygame.display.set_icon(icono)

# ICONO DE JUGADOR
img_jugador = pygame.image.load("./DÍA10-INVASIÓN-ESPACIAL/cohete.png")
# variable del jugador
jugador_x = 368
jugador_y = 510
jugador_x_cambio = 0

# variable del enemigo
img_enemigo = pygame.image.load("./DÍA10-INVASIÓN-ESPACIAL/enemigo64.png")
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 0.5
enemigo_y_cambio = 50

# funcion jugador 
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# funcion enemigo 
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

# LOOP DEL JUEGO
se_ejecuta = True 
while se_ejecuta:
    # imagen de fondo
    pantalla.blit(fondo, (0, 0))
    # RGB COLOR DE FONDO
    # pantalla.fill((250, 242, 7))
    # jugador_x += 0.10
     
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
                jugador_x_cambio = .05
        # evento soltar flechas
        # KEYUP
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                # print("flecha fue soltada")
                jugador_x_cambio = 0
    # modificar lugar del jugador
    jugador_x += jugador_x_cambio

    # mantener dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # modificar lugar del enemigo
    enemigo_x += enemigo_x_cambio

    # mantener dentro de bordes
    if enemigo_x <= 0:
        enemigo_x_cambio = .05
        enemigo_y += enemigo_y_cambio
        enemigo_y
    elif enemigo_x >= 736:
        enemigo_x_cambio = -.05
        enemigo_y += enemigo_y_cambio


    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # actualizar
    pygame.display.update()