import time
import turtle
from turtle import Screen
from Snake import Snake
from food import food
from Scoreboard import Scoreboard

canvas = Screen()
canvas.screensize(600, 600)
canvas.tracer(0)
canvas.bgcolor("black")
gameState=True
snake = Snake()
food = food()
scoreboard = Scoreboard()
snake.setup()

def gameOff():
    global gameState
    gameState=not gameState

while gameState:
    canvas.update()
    time.sleep(0.1)
    snake.move()

#if the snake head collides with food add another piece to the body
    if snake.snakeBody[0].distance(food)< 15.9:
        food.change_position()
        snake.addToBody()
        scoreboard.score_up()

#if the snake head collides with the wall end the game
    if snake.snakeBody[0].xcor() < -400 or snake.snakeBody[0].xcor() > 400 or snake.snakeBody[0].ycor() < -400 or snake.snakeBody[0].ycor() > 400 :
        gameState=False
        scoreboard.game_over()
    for i in range(len(snake.snakeBody)-1,0 , -1):
        if snake.snakeBody[0].distance(snake.snakeBody[i])<10:
            gameState = False
            scoreboard.game_over()


    canvas.listen()
    canvas.onkeypress(key="Left" , fun=snake.turnLeft)
    canvas.onkeypress(key="Right", fun=snake.turnRight)










canvas.exitonclick()
