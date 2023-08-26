import pygame
import random
import time

velocidad = 10

ventanaX = 720
ventanaY = 480

Negro = pygame.Color(0,0,0)
Naranja = pygame.Color(255, 255, 255)
verde = pygame.Color(0, 255, 0)
rojo = pygame.Color(255, 0, 0)
                 
pygame.init()


pygame.display.set_caption("Vivora")
game_ventana = pygame.display.set_mode((ventanaX, ventanaY))

fps = pygame.time.Clock()

posicion_vivora = [100,50]

cuerpo_vivora = [[100, 50],
                 [90, 50],
                 [80, 50],
                 [70, 50]]

posicion_fruta  = [random.randrange(1, (ventanaX//10))* 10,
                   random.randrange(1, (ventanaY//10))* 10]

reaparecer_fruta = True

direccion = "RIGHT"
cambio = direccion

Puntos = 0

def mostrar_puntos(cambio, color, font, size):

    fuente_puntos = pygame.font.SysFont(font, size)

    puntos_surface = fuente_puntos.render("Puntos: " + str(Puntos), True, color)

    puntos_rect = puntos_surface.get_rect()

    game_ventana.blit(puntos_surface, puntos_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)

    game_over_surface = my_font.render(
        'Puntos logrados: ' + str(Puntos), True, rojo
    )

    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (ventanaX/2, ventanaY/4)

    game_ventana.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)

    pygame.quit()

    quit()

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cambio = 'UP'
            if event.key == pygame.K_DOWN:
                cambio = 'DOWN'
            if event.key == pygame.K_LEFT:
                cambio = 'LEFT'
            if event.key == pygame.K_RIGHT:
                cambio = 'RIGHT' 
    
    if cambio == 'UP' and direccion != 'DOWN':
        direccion = 'UP'
    if cambio == 'DOWN' and direccion != 'UP':
        direccion = 'DOWN'
    if cambio == 'LEFT' and direccion != 'RIGHT':
        direccion = "LEFT"
    if cambio == 'RIGHT' and direccion != 'LEFT':
        direccion = 'RIGHT'

    if direccion == 'UP':
        posicion_vivora[1] -=10
    if direccion == 'DOWN':
        posicion_vivora[1] +=10
    if direccion == 'LEFT':
        posicion_vivora[0] -=10
    if direccion == 'RIGHT':
        posicion_vivora[0] +=10

    cuerpo_vivora.insert(0, list(posicion_vivora))
    if posicion_vivora[0] == posicion_fruta[0] and posicion_vivora[1] == posicion_fruta[1]:
        Puntos += 10
        reaparecer_fruta = False
    else:
        cuerpo_vivora.pop()
    
    if not reaparecer_fruta:
        posicion_fruta  = [random.randrange(1, (ventanaX//10))* 10,
                           random.randrange(1, (ventanaY//10))* 10]
    
    reaparecer_fruta = True
    game_ventana.fill(Naranja)

    for pos in cuerpo_vivora:
        pygame.draw.rect(game_ventana, verde,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_ventana, rojo, pygame.Rect(
        posicion_fruta[0], posicion_fruta[1], 10,10
    ))

    if posicion_vivora[0] < 0 or posicion_vivora[0] > ventanaX-10:
        game_over()
    if posicion_vivora[1] <0 or posicion_vivora[1] > ventanaY-10:
        game_over()

    for block in cuerpo_vivora[1:]:
        if posicion_vivora[0] == block[0] and posicion_vivora[1] == block[1]:
           game_over()

    mostrar_puntos(1, Negro, 'times new roman', 20)

    pygame.display.update()

    fps.tick(velocidad)

                 






