from turtle import Turtle, Screen

tim = Turtle()

for _ in range(15):
    tim.forward(10)
    # Move sem escrever
    tim.penup()
    tim.forward(10)
    # Comaca a escrever novamente
    tim.pendown()

screen = Screen()
screen.exitonclick()