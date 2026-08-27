# This code is for a challenge on reeborg where he has to make it through a maze @ https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# This code allows the robot to turn right as there is no function for it
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# within this code it tells the robot to basically stick to the right hand wall of the maze allowing it to reach the goal everytime.
while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right()
        move()