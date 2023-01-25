import random
from turtle import Turtle
class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5 , stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.random_x = random.randint(-200,200)
        self.random_y = random.randint(-200,200)
        self.goto(self.random_x,self.random_y)

    def return_position(self):
        position = (self.random_x , self.random_y)
        return position

    def change_position(self):
        self.random_x = random.randint(-200, 200)
        self.random_y = random.randint(-200, 200)
        self.goto(self.random_x, self.random_y)
