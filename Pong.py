import turtle

ninja = turtle.Screen()
ninja.title("Pong by @_lewis_ew_")
ninja.bgcolor("white")
ninja.setup(width=800, height=600)
ninja.tracer(0)

# Sets scores to 0 at the beginnig of the game
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=3, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=3, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = -0.25

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.color("red")
pen.write("Player A: 0", align="right", font=("Courier", 24, "normal"))
pen.color("blue")
pen.write("Player B: 0", align="left", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard Binding
ninja.listen()
ninja.onkeypress(paddle_a_up, "w")
ninja.onkeypress(paddle_a_down, "s")
ninja.onkeypress(paddle_b_up, "Up")
ninja.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    ninja.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.color("red")
        pen.write("Player A: {} ".format(score_a), align="right", font=("Courier", 24, "normal"))
        pen.color("blue")
        pen.write("Player B: {}".format(score_b), align="left", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.color("red")
        pen.write("Player A: {} ".format(score_a), align="right", font=("Courier", 24, "normal"))
        pen.color("blue")
        pen.write("Player B: {}".format(score_b), align="left", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
