from turtle import Screen
from score import Score
from food import Food
from snake import Snake
import time

game_on = True

win = Screen()
score = Score()
food = Food()
snake = Snake()
win.title("Snake Game")
win.bgcolor("black")
win.tracer(0)
win.setup(600,600)

snake.create_snake()

win.listen()
win.onkey(snake.move_up, "Up")
win.onkey(snake.move_down, "Down")
win.onkey(snake.move_left, "Left")
win.onkey(snake.move_right, "Right")

while game_on:
    snake.move_snake()
    win.update()
    time.sleep(0.1)

    x_outside = snake.snake_body[0].xcor() >= 280 or snake.snake_body[0].xcor() <= -280
    y_outside = snake.snake_body[0].ycor() >= 280 or snake.snake_body[0].ycor() <= -280

    if x_outside or y_outside:
        game_on = False

    if snake.snake_body[0].distance(food.snake_food) < 15:
        food.food_refresh()
        score.update_score()

win.mainloop()
