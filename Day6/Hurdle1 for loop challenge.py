#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def up():
    move()
    turn_left()
def right():
    move()
    turn_left()
    turn_left()
    turn_left()
def game():
    up()
    right()
    right()
    up()
for i in range(1,7):
    game()