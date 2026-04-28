############################################ Meu Jeito ######################################3

### Easy

# Funcao para virar a direita
def turn_right():     
    for n in range(3):
        turn_left()

# Enquanto nao chegar no ponto desejada
while not at_goal():
    # Se a direita estiver livre vai virar a direita
    if right_is_clear():
        turn_right()
    # Enquento bater na parede, vai virar a esquerda
    while wall_in_front():
        turn_left()
    # Caminho limpo = move
    move()

### Desafio: Mapa 1 e 2

def turn_right():
    for n in range(3):
        turn_left()

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
        while wall_in_front():
            turn_left()

### Desafio: Mapa 1 2 e 3

def turn_right():
    for n in range(3):
        turn_left()

while not at_goal():
    # Unica diferenca: Sempre que a frente estiver livre o robo se move
    while front_is_clear():
        move()
    if right_is_clear():
        turn_right()
    while wall_in_front():
        turn_left()

######################################## Tutor way #########################################

### Easy

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

### Desafio 1, 2 e 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
