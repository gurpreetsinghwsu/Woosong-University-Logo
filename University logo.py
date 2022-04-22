import turtle

screen = turtle.Screen()
screen.bgcolor("White")
screen.setup(width=550, height=550)
screen.title("Woosong")

my_turtle = turtle.Turtle()
my_turtle.pensize(30)
my_turtle.shape("arrow")

my_turtle.penup()
my_turtle.goto(-250, -90)

my_turtle.pendown()

my_turtle.color("green")

my_turtle.circle(80)
my_turtle.penup()
my_turtle.forward(100)



my_turtle.left(0)
my_turtle.pendown()
my_turtle.pencolor("blue")
my_turtle.left(50)
my_turtle.forward(200)
my_turtle.right(100)
my_turtle.forward(200)


my_turtle.penup()
my_turtle.left(50)
my_turtle.forward (100)
my_turtle.pendown()
my_turtle.pencolor("red")
my_turtle.forward(100)
my_turtle.backward(150)
my_turtle.left(90)
my_turtle.forward(150)
my_turtle.right(90)
my_turtle.forward(150)
turtle.done()