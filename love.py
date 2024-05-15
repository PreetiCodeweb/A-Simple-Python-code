import turtle

def draw_heart():
    turtle.color('red')
    turtle.begin_fill()
    turtle.fillcolor('red')
    turtle.left(140)
    turtle.forward(224)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(224)
    turtle.end_fill()

# Set up the turtle window
turtle.speed(2)
turtle.bgcolor('white')

# Draw the heart
draw_heart()

# Hide the turtle and display the window
turtle.hideturtle()
turtle.done()
