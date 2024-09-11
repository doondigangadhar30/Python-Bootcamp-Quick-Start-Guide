#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
def go():
    while front_is_clear():
        if at_goal():
            break
        else:
            move()
    while wall_in_front():
        jump()
def right():
    move()
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    right()
    right()
    move()
    turn_left()
    up()
while not at_goal():
    go()