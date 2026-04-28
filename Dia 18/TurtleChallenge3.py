from turtle import Turtle, Screen
import random

colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", 
          "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

class Geometric:
    def __init__(self):
        self.lados = 3
    
    # Podia tem feito um for com uma range de 3 pra 11
    def aumenta_lado(self):
        self.lados += 1
    
    def angulo(self):
        angulo = 360 / self.lados
        return angulo
    
    def parada(self):
        return self.lados <= 10

tim = Turtle()
figura_geo = Geometric()

# Meio que arrasei nessa
while figura_geo.parada():
    color = random.choice(colors)
    tim.pencolor(color)
    for _ in range(figura_geo.lados):
        tim.forward(100)
        tim.right(figura_geo.angulo())
    figura_geo.aumenta_lado()

screen = Screen()
screen.exitonclick()