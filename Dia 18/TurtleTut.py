from turtle import Turtle, Screen

# Objeto da classe Turtle() -> A tartaruguinha que fica na tela
timmy_the_turtle = Turtle() 
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)

# Objeto da classe Scream -> A tela onde a tartaruga fica
screen = Screen()
screen.exitonclick()