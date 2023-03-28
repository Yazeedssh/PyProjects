#In this prorgram I helped the lost Robot in the maze to find the exit out of the maze in Reeborg's World website

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def goo():
    
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
        if wall_in_front():
            turn_left()
        move()
    elif front_is_clear():
        move()
    else:
        while wall_on_right():
            move()
            
while not at_goal():
    goo()