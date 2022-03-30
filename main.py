from turtle import Screen
import time
from snake import Snake
from food import Food
from ScoreBoard import ScoreBoard

#SETTING UP INITIAL SCREEN
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("SNAKE GAME")
screen.tracer(0)

#CREATING SHAPE OF OUR SNAKE
snake = Snake()

#CREATING THE FOOD
hrana = Food()

#CREATING SCOREBOARD
display = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#MOVING OUR SNAKE
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    #Detect Collision
    if snake.segments[0].distance(hrana) < 15:
        hrana.change_position()
        snake.eating()
        display.point_scored()

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() <-290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        game_is_on = False
        display.game_over()

    for i in range(1,len(snake.segments)):
        if snake.segments[0].distance(snake.segments[i]) < 10:
            game_is_on = False
            display.game_over()

screen.exitonclick()