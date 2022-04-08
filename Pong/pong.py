import turtle
import os

paddle_move_speed = 20
ball_move_speed = .05

wn = turtle.Screen()
wn.title("Pong by Robert Bagwell")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ball_move_speed
ball.dy = ball_move_speed

#Scores
score_a = 0
score_b = 0

#Scoreboard
scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.color("white")
scoreBoard.penup()
scoreBoard.hideturtle()
scoreBoard.goto(0, 260)
scoreBoard.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

#Move Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += paddle_move_speed
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= paddle_move_speed
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += paddle_move_speed
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= paddle_move_speed
    paddle_b.sety(y)    


#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main Game Loop
while True:
    wn.update()
    #move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Check 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")
    elif ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1 
        os.system("aplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        scoreBoard.clear()
        scoreBoard.write(f"Player 1: {score_a}  Player 2: {score_b}", align="center", font=("Courier", 24, "normal"))
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        scoreBoard.clear()
        scoreBoard.write(f"Player 1: {score_a}  Player 2: {score_b}", align="center", font=("Courier", 24, "normal"))

    #Paddle Boundry Check
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    elif paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    elif paddle_a.ycor() < -250:
        paddle_a.sety(-250)        

    #Ball Paddle Collision
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        os.system("aplay bounce.wav&") 
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("aplay bounce.wav&")