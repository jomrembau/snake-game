from turtle import Turtle

class Snake:

    def __init__(self):
        self.snake_tail = []
        self.x = 0

    def create_snake(self):
        for segment in range(1,4):
            segment = Turtle()
            segment.penup()
            segment.shape("square")
            segment.shapesize(0.6)
            segment.color("white")
            segment.goto(x=self.x, y=0)
            self.x += 13
            self.snake_tail.append(segment)

