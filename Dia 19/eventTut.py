from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

# Olha o que o usiario manda
screen.listen()

# Funcoes usadas com parametro, tem como passar uma funcao como parametro pra outra
# Como usar uma funcao em outra?
## So chamar ela na funcao como qualquer outra
## Ex:
## def calculator(n1, n2, func):   -> func pode ser qualquer funcao de calculo
##      return func(n1, n2)
# Nao colocar () na hora de colocar de parametro
# - Higher order function -

screen.onkey(key = "space", fun = move_forward)
screen.exitonclick()