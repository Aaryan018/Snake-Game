from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.change_location()

    def change_location(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.setpos(new_x, new_y)