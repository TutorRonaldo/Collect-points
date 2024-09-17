from random import randint

import pgzrun
from pgzero.actor import Actor

# Definir las dimensiones de la ventana del juego
WIDTH = 600
HEIGHT = 600

# Inicializar la puntuación, la velocidad del personaje y el tiempo de juego
score = 0
velocidad = 4
tiempo = 20

# Inicializar el estado del juego
game_over = False
game_started = False

# Crear el actor "mario" y establecer su posición inicial
mario = Actor("mario")
mario.pos = 100, 100

# Crear el actor "hongo" y establecer su posición inicial
hongo = Actor("hongo")
hongo.pos = 200, 200

def draw():
    if game_started:
        # Dibujar el fondo del juego
        screen.blit("background", (0, 0))

        # Dibujar los actores "mario" y "hongo"
        mario.draw()
        hongo.draw()

        # Dibujar la puntuación y el tiempo en la pantalla
        screen.draw.text("Score:" + str(score), color="black", topleft=(10, 10))
        screen.draw.text("Tiempo:" + str(tiempo), color="black", topleft=(10, 30))

        # Si el juego ha terminado, detener la velocidad y mostrar la puntuación final
        if game_over:
            velocidad = 0
            screen.blit("background", (0, 0))
            screen.draw.text("Final Score:" + str(score), topleft=(180, 250), fontsize=60, color="black")
            screen.draw.text("Presiona R para reiniciar", topleft=(180, 320), fontsize=30, color="black")
    else:
        # Dibujar la pantalla de inicio
        screen.blit("background", (0, 0))
        screen.draw.text("Presiona G para comenzar", topleft=(180, 250), fontsize=30, color="black")

def place_hongo():
    # Colocar el "hongo" en una posición aleatoria dentro de los límites de la pantalla
    hongo.x = randint(20, (WIDTH - 20))
    hongo.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over, tiempo
    if tiempo:
        tiempo = tiempo - 1
    else:
        # Establecer el estado del juego a terminado
        game_over = True

def reset_game():
    global score, tiempo, game_over, game_started
    score = 0
    tiempo = 20
    game_over = False
    game_started = True
    mario.pos = 100, 100

def update():
    global score, game_started, game_over, tiempo
    if game_started:
        # Mover el "mario" en función de las teclas presionadas
        if keyboard.left:
            mario.x -= velocidad
        if keyboard.right:
            mario.x += velocidad
        if keyboard.up:
            mario.y -= velocidad
        if keyboard.down:
            mario.y += velocidad

        # Comprobar si "mario" ha recogido el "hongo"
        hongo_collected = mario.colliderect(hongo)

        # Si el "hongo" es recogido, aumentar la puntuación y colocar el "hongo" en una nueva posición
        if hongo_collected:
            score += 10
            place_hongo()
    else:
        if keyboard.G:
            game_started = True
            tiempo = 20
        
    # Permitir reiniciar el juego presionando la tecla R cuando el juego ha terminado
    if game_over and keyboard.R:
        reset_game()

clock.schedule_interval(time_up, 1)
place_hongo()
# Iniciar el juego con PGZRun
pgzrun.go()

