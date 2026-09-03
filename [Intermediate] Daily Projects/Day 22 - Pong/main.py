import userint
import paddle
import time
import ball_data

# Gamestate var
gameOn = True

# Interface setup
userInterface = userint.UserInterface()
scoreboard = userint.Scoreboard()

# Player paddle setup
player1 = paddle.Paddle()
player2 = paddle.Paddle()
player1.playerID = 1
player2.playerID = 2
player1.set_location()
player2.set_location()

# Ball setup
ball = ball_data.Ball()



# Control Scheme
userInterface.screen.listen()
userInterface.screen.onkeypress(player1.move_up, "w")
userInterface.screen.onkey(player1.move_down, "s")
userInterface.screen.onkey(player2.move_up, "i")
userInterface.screen.onkey(player2.move_down, "k")

# Game Loop
while gameOn:
    time.sleep(0.01)
    userInterface.screen.update()
    ball.move()

    if player1.check_overlap(ball):
        print("Player 1 wins!")
        ball.ball_rebound(1)
    if player2.check_overlap(ball):
        print("Player 2 wins!")
        ball.ball_rebound(2)

    if ball.xcor() > userint.SCREEN_WIDTH/2:
        scoreboard.update_score(player1.playerID)
        ball.reset()
    elif ball.xcor() < -userint.SCREEN_WIDTH/2:
        scoreboard.update_score(player2.playerID)
        ball.reset()

userInterface.screen.exitonclick()
