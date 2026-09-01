from turtle import Turtle, Screen
import time
import snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("SNAEK GAEME")
isRunning = True
screen.update()
snake = snake.Snake()

while isRunning:
    time.sleep(0.1)
    snake.move_forward()
    screen.update()
    screen.onkeypress(snake.move_left, "j")
    screen.onkeypress(snake.move_right, "l")
    screen.onkeypress(snake.move_up, "i")
    screen.onkeypress(snake.move_down, "k")
    screen.listen()
screen.exitonclick()