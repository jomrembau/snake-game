from turtle import Turtle
import random

class Food:

    def __init__(self):
        self.pos_x = random.randint(-14, 14) * 20
        self.pos_y = random.randint(-14, 14) * 20
        self.snake_food = Turtle()
        self.snake_food.penup()
        self.snake_food.shape("circle")
        self.snake_food.color("blue")
        self.snake_food.shapesize(0.4)
        self.snake_food.goto(x=self.pos_x, y=self.pos_y)

    def food_refresh(self):
        self.pos_x = random.randint(-12, 12) * 20
        self.pos_y = random.randint(-12, 12) * 20
        self.snake_food.goto(x=self.pos_x, y=self.pos_y)
