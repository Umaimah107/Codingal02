import turtle 
turtle.Screen().bgcolor("pink")
board = turtle.Turtle()

#triangle
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

#square
board.pencolor("darkpink")
board.forward(100)
board.left(90)
board.forward(100)
board.left(90)
board.forward(100)
board.left(90)
board.forward(100)


turtle.done()