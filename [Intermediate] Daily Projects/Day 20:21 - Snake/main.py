from turtle import Turtle, Screen
import time
import snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("SNAEK GAEME")
snakeBody = []
isRunning = True
screen.update()

snake = snake.Snake()

while isRunning:
    time.sleep(0.1)
    snake.move_forward()
    screen.update()
screen.exitonclick()