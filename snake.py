from turtle import Turtle

class Snake:

    def __init__(self):
        self.snake_body = []
        self.x = 0

    def create_snake(self):
        for segment in range(1,4):
            segment = Turtle()
            segment.penup()
            segment.shape("square")
            segment.shapesize(1)
            segment.color("white")
            segment.goto(x=self.x, y=0)
            self.x += 20
            self.snake_body.append(segment)

    def add_segment(self):
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.shapesize(1)
        segment.color("white")
        tail = self.snake_body[-1]
        segment.goto(tail.xcor(), tail.ycor())
        self.snake_body.append(segment)

    def move_snake(self):
        for x in range(len(self.snake_body)-1,0,-1):
            new_xcor = self.snake_body[x - 1].xcor()
            new_ycor = self.snake_body[x - 1].ycor()
            self.snake_body[x].goto(new_xcor, new_ycor)
        self.snake_body[0].forward(20)

    def move_up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def move_down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def move_right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def move_left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def body_collision(self):
        for segment in self.snake_body[1:]:
            if self.snake_body[0].distance(segment) < 10:
                return True
        return False

    def reset_snake(self):
        for segment in self.snake_body:
            segment.goto(1000, 1000)
        self.snake_body.clear()
        self.x = 0





