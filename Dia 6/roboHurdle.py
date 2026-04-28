def turn_right():
    for n in range(3):
        turn_left()

def jump():
    while wall_in_front():
        turn_left()
        move()
        turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
      
while at_goal() == False:
    
    if wall_in_front():
        jump()
    else:
        move()