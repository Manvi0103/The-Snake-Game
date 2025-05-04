from turtle import Turtle, Screen
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect collision with food
    if snake.turtles[0].distance(food) < 15:
        snake.tail()
        food.refresh()
        scoreboard.update_score()

    #detect collision with wall
    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -280 or snake.turtles[0].ycor() > 280 or snake.turtles[0].ycor() < -280:
        game_on = False
        scoreboard.game_over()

    #detect collision with its own tail
    # for segment in snake.turtles:
    #     if segment == snake.turtles[0]:
    #         pass
    #     elif snake.turtles[0].distance(segment) < 10:
    #         game_on = False
    #         scoreboard.game_over()

    for segment in snake.turtles[1:]:
        if snake.turtles[0].distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
 
screen.exitonclick()
