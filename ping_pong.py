#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: ping_pong.py
Author: Jorge Ruiz.
"""

import turtle


# Aquí lo que hacemos es un "objecto" para poder manipular los atributos de la pantalla.
window = turtle.Screen()

# Definimos la pantalla del juego.
window.title('Ping Pong Game by Jorge Ruiz')
window.bgcolor('black')
# (anchura, altura)
window.setup(width = 800, height = 600)
window.tracer(0)


# Marcador
score_a = 0
score_b = 0


# Jugador A
player_a = turtle.Turtle()
player_a.speed(0)
# Aquí definimos que forma va a ser el jugador A.
# shape define la figura mientras que shapesize define el tamaño.
player_a.shapesize(stretch_wid = 5, stretch_len = 1)
player_a.shape('square')
player_a.color('white')
# nos permite mover al jugador sin dibujar lineas de recorrido.
player_a.penup()
# El primer número define la posición del jugador izq-der, el segundo de arriba-abajo
# en este caso a la izquierda y el centro.
player_a.goto(-350, 0)


# Jugador B
player_b = turtle.Turtle()
player_b.speed(0)
# Aquí definimos que forma va a ser el jugador A.
# shape define la figura mientras que shapesize define el tamaño.
player_b.shapesize(stretch_wid = 5, stretch_len = 1)
player_b.shape('square')
player_b.color('white')
# nos permite mover al jugador sin dibujar lineas de recorrido.
player_b.penup()
# El primer número define la posición del jugador izq-der, el segundo de arriba-abajo
# en este caso a la derecha y el centro.
player_b.goto(350, 0)


# Pelota
ball = turtle.Turtle()
ball.speed(0)
# Aquí definimos que forma va a ser el jugador A.
# shape define la figura mientras que shapesize define el tamaño.
#ball.shapesize(stretch_wid = .7, stretch_len = .7)
ball.shape('square')
ball.color('white')
# nos permite mover al jugador sin dibujar lineas de recorrido.
ball.penup()
# El primer número define la posición del jugador de izq-der, el segundo de arriba-abajo
# en este caso está en el centro.
ball.goto(0, 0)
# Movimiento de la pelota en direcciones y velocidad de movimiento.
ball.dx = .07
ball.dy = -.07


# Apuntador
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
# Poner aquí el nombre de los jugadores.
pen.write("Player A: 0    Player B: 0", align = "center", font = ("Courier", 15, "normal"))


'''
Ahora definimos las funciones para el movimiento de los jugadores.
'''
# Jugador A.
def player_a_up():
    move_up = player_a.ycor()
    move_up += 20
    player_a.sety(move_up)

def player_a_down():
    move_down = player_a.ycor()
    move_down -= 20
    player_a.sety(move_down)

# Jugador B.
def player_b_up():
    move_up = player_b.ycor()
    move_up += 20
    player_b.sety(move_up)

def player_b_down():
    move_down = player_b.ycor()
    move_down -= 20
    player_b.sety(move_down)


'''
Aquí realizaremos el movimiento detectando las teclas a presionar respectivamente.
'''
window.listen()
window.onkeypress(player_a_up, "w")
window.onkeypress(player_a_down, "s")
window.onkeypress(player_b_up, "Up")
window.onkeypress(player_b_down, "Down")



# Ciclo para mantener la pantalla del juego todo el tiempo.
game = True
while game:
    try:
        window.update()
    except:
        pass

    # Movimiento de la pelota.
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    ''' Definimos los marcos de la aplicación. '''
    # Como la ultura es de 600, entonces nos iremos a la mitad arriba y mitad abajo
    # y como la anchura es de 800 igual nos iremos a la mitad izq. y mitad der.

    # Aquí hacemos que los jugadores no puedan desaparecer del mapa (salirse del cuadro).
    if player_a.ycor() > 260:
        player_a.sety(260)
    elif player_a.ycor() < -260:
        player_a.sety(-260)
    elif player_b.ycor() > 260:
        player_b.sety(260)
    elif player_b.ycor() < -260:
        player_b.sety(-260)


    # Cuando la bola va para arriba.
    if ball.ycor() > 290:
        # Damos la posición.
        ball.sety(290)
        # Hacemos que se dirija al lado contrario, en este caso que baje.
        ball.dy *=-1

    # Cuando la bola va para abajo.
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Cuando la bola va para la derecha.
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dy *=-1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 15, "normal"))

    # Cuando la bola va para la izquierda.
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dy *=-1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 15, "normal"))



    ''' Ahora definiremos el movimiento de la pelota al chocar con un jugador. '''

    # Choque con jugador B.
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_b.ycor() + 40 and ball.ycor() > player_b.ycor() -40):
        ball.setx(340)
        ball.dx *=-1

    # Choque con jugador A.
    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < player_a.ycor() + 40 and ball.ycor() > player_a.ycor() -40):
        ball.setx(-340)
        ball.dx *=-1
