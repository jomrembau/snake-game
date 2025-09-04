from turtle import Screen
from score import Score
from food import Food
from snake import Snake

first_move = True
win = Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(600, 600)
win.tracer(0)

score = Score()
food = Food()
snake = Snake()
snake.create_snake()
snake.snake_body[0].setheading(0)  # head faces right

win.listen()
win.onkey(snake.move_up, "Up")
win.onkey(snake.move_down, "Down")
win.onkey(snake.move_left, "Left")
win.onkey(snake.move_right, "Right")

def game_loop():
    global first_move
    snake.move_snake()
    win.update()

    if abs(snake.snake_body[0].xcor()) >= 270 or abs(snake.snake_body[0].ycor()) >= 270:
        print("Game Over: Hit Wall")
        return
    if not first_move and snake.body_collision():
        print("Game Over: Hit Body")
        return

    if snake.snake_body[0].distance(food.snake_food) < 15:
        food.food_refresh()
        score.update_score()
        snake.add_segment()

    first_move = False
    win.ontimer(game_loop, 100)

game_loop()
win.mainloop()
