import time
from turtle import Turtle , Screen


class Snake():
    def __init__(self):
        self.starting_pos = [(0, 0), (-20,0), (-40, 0)]
        self.snakeBody = []

    def setup(self):
        for pos in self.starting_pos:
            piece = Turtle(shape="square")
            piece.color("white")
            piece.penup()
            piece.goto(pos)
            self.snakeBody.append(piece)

    def move(self):
            for i in range(len(self.snakeBody)-1,0 , -1):
                newX=self.snakeBody[i-1].xcor()
                newY=self.snakeBody[i-1].ycor()
                self.snakeBody[i].goto(newX,newY)

            self.snakeBody[0].forward(20)

    def turnLeft(self):
        self.snakeBody[0].left(90)
    def turnRight(self):
        self.snakeBody[0].right(90)

    def addToBody(self):
        piece = Turtle(shape="square")
        piece.color("white")
        piece.penup()
        piece.goto((self.snakeBody[-1].xcor()-20),(self.snakeBody[-1].ycor()))
        self.snakeBody.append(piece)

    def head_position(self):
        position= (self.snakeBody[0].xcor(),self.snakeBody[0].ycor())
        return position
    def reset(self):
        for seg in self.snakeBody:
            seg.goto(1000,1000)
        self.snakeBody.clear()
        self.setup()






