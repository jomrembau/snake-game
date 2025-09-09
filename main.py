from turtle import Screen
from score import Score
from food import Food
from snake import Snake
import os


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
        score.update_high()
        score.reset_score()
        snake.reset_snake()
        snake.create_snake()
        snake.move_snake()


    if not first_move and snake.body_collision():
        score.update_high()
        score.reset_score()
        snake.reset_snake()
        snake.create_snake()
        snake.move_snake()

    if snake.snake_body[0].distance(food.snake_food) < 15:
        score.update_score()
        score.update_high()
        food.food_refresh()
        snake.add_segment()

    first_move = False
    win.ontimer(game_loop, 100)

if os.path.exists("highscore.txt"):
    with open("highscore.txt", "r") as f:
        try:
            score.highscore = int(f.read())
        except:
            score.highscore = 0
else:
    score.highscore = 0

score.score_text.clear()
score.score_text.write(f"Score: {score.score} | HighScore: {score.highscore}", font=("Courier", 16, ""), align="center")





game_loop()
win.mainloop()
