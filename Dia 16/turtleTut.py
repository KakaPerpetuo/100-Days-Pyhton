# Existe uma classe declarada nesse turtle
import turtle

# CRIAR UM OBJETO - Que fica no meio da tela
timmy = turtle.Turtle()
# Chamando o metodo
timmy.shape("turtle")
timmy.color("hotpink")
timmy.forward(100)

# Cria o objeto da tela
my_screen = turtle.Screen()
print(my_screen.canvheight)

# Method
my_screen.exitonclick()