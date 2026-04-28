from turtle import Turtle, Screen

timmy = Turtle()

# Desenhar um quadrado com o timmy
for i in range(4):
    timmy.forward(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()