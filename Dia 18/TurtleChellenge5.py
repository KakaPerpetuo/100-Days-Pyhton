from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
colormode(255)
tim.speed("fastest")

contador = 0

# Funcao que cria uma cor aleatoria usando as 3 cores primarias
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # Coloca uma tupla
    color = (r, g, b)
    return color

# Tinha como fazer usando a funcao heading para mudar a posicao
# Tinha como fazer uma funcao que passa de parametro o tamanho do espaco entre os circulos, esse tamanho é dividido por 360 pra saber onde parar
while contador < (360/5):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.right(5)
    contador += 1

screen = Screen()
screen.exitonclick()