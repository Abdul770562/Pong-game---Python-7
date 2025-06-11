# import time
# from turtle import Screen
#
# from snake import Snake
# from food import Food
# from scoreboard import  Scoreboard
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My snake Game")
# screen.tracer(0)
#
#
#
# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()
# screen.listen()
#
# screen.onkey(snake.up  ,"Up")
# screen.onkey(snake.down  ,"Down")
# screen.onkey(snake.left  ,"Left")
# screen.onkey(snake.right  ,"Right")
#
# is_moving = True
# while is_moving:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.score_count()
#
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         scoreboard.reset()
#         snake.reset()
#
#     for segment in snake.segments:
#         if segment == snake.head:
#             pass
#         elif snake.head.distance(segment) < 10:
#             scoreboard.reset()
#             snake.reset()

import time
import json
import winsound  # For sound effects (Windows)
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def play_sound(sound_file):
    """Plays a sound effect."""
    try:
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    except:
        pass  # If sound fails, continue without it


# Ask player for difficulty
difficulty = Screen().textinput("Choose Difficulty", "Enter: Easy / Medium / Hard").lower()
difficulty_speeds = {"easy": 0.15, "medium": 0.1, "hard": 0.05}
game_speed = difficulty_speeds.get(difficulty, 0.1)  # Default to Medium

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Improved Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_moving = True
while is_moving:
    screen.update()
    time.sleep(game_speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_count()
        play_sound("food.wav")  # Play eating sound
        game_speed *= 0.95  # Increase difficulty

    # Detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        play_sound("game_over.wav")  # Play collision sound
        time.sleep(2)
        scoreboard.reset()
        snake.reset()
        game_speed = difficulty_speeds.get(difficulty, 0.1)  # Reset speed

    # Detect collision with tail
    for segment in snake.segments[1:]:  # Ignore head
        if snake.head.distance(segment) < 10:
            play_sound("game_over.wav")
            time.sleep(2)
            scoreboard.reset()
            snake.reset()
            game_speed = difficulty_speeds.get(difficulty, 0.1)

screen.exitonclick()
