from turtle import Turtle, Screen, colormode
import random

turn = [0, 90, 180, 270]

thickness = 15
speed = 1

tim = Turtle()
colormode(255)

# Funcao que cria uma cor aleatoria usando as 3 cores primarias
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # Coloca uma tupla
    color = (r, g, b)
    return color

for _ in range(300):
    tim.forward(30)
    tim.pencolor(random_color())
    # thickness += 1
    # Era so pra aumentar uma vez
    tim.pensize(thickness)
    speed += 1
    tim.speed(speed)
    # Dava pra ter usado a funcao setheading -> escolhia angulo pra virar
    sorted_direction = random.randint(0, 1)
    if sorted_direction == 1:
        tim.right(random.choice(turn))
    else:
        tim.left(random.choice(turn))

screen = Screen()
screen.exitonclick()