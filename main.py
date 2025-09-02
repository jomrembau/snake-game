from turtle import Screen
from score import Score
from food import Food
from snake import Snake

win = Screen()
score = Score()
food = Food()
snake = Snake()
win.title("Snake Game")
win.bgcolor("black")
win.tracer(0)
win.setup(600,600)

snake.create_snake()
win.update()

win.mainloop()