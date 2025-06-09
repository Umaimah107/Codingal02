from turtle import * 

class Face:

    def __init__(self, xpos, ypos):
        self.size = 90
        self.coord = (xpos, ypos)

    def setSize(self, radius):
            self.size = radius

    def draw(self):
         self.gohome()
         pensize(4)
         speed(0)
         self.drawOutline()

    def gohome(self):
         penup()
         goto(self.coord)

         setheading(0)

    def drawOutline(self):
         penup()
         forward(self.size)
         left(90)
         pendown()
         circle(self.size)
         self.gohome()    

f1 = Face(0,0)
f1.draw()

showturtle()
done()
