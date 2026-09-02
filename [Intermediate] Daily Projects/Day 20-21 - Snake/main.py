import userinterface
import time
import snake
import food

# Gamestate variable
isRunning = True

#Sets UI pieces
userWindow = userinterface.UserInterface()
scoreboard = userinterface.Scoreboard()

# sets up snake and food
snake = snake.Snake()
food = food.Food()

# Sets keybindings
userWindow.screen.listen()
userWindow.screen.onkeypress(snake.move_left, "j")
userWindow.screen.onkeypress(snake.move_right, "l")
userWindow.screen.onkeypress(snake.move_up, "i")
userWindow.screen.onkeypress(snake.move_down, "k")



while isRunning:
    #Deals with automatic movement
    userWindow.screen.update()
    time.sleep(0.1)
    snake.move_forward()

    # Deals with adding score from food
    if snake.head.distance(food) < 18:
        food.reset_position()
        scoreboard.add_score()
        snake.add_segment(len(snake.body))

    # Deals with hitting walls
    if snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() > 280 or snake.head.xcor() < -280:
        isRunning = False
        scoreboard.game_over()

    # Deals with ouroboros situation
    for parts in snake.body[1:]:
        if snake.head.distance(parts) < 20:
            isRunning = False
            scoreboard.game_over()

userWindow.screen.exitonclick()
