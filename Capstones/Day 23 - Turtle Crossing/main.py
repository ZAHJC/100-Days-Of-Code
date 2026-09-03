import time
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
STARTING_CAR_AMOUNT = 6
loopTimer = 0
carList = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

torti = Player()

scoreboard = Scoreboard()

for i in range(STARTING_CAR_AMOUNT):
    carList.append(Car())

screen.listen()
screen.onkeypress(torti.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)

    if loopTimer == 6:
        carList.append(Car())
        loopTimer = 0

    for car in carList:
        car.move()

    for car in carList:
        if car.check_collision(torti):
            scoreboard.game_over()
            game_is_on = False

    if torti.ycor() > 285:
        torti.next_level()
        scoreboard.add_score()
        for car in carList:
            car.increase_speed()

    for car in carList:
        if car.xcor() < -310:
            car.hideturtle()
            carList.remove(car)
    screen.update()
    loopTimer += 1

screen.exitonclick()