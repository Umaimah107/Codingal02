class Circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 *self.radius* self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius 
r = float(input("Enter the radius of the circle: "))
c = Circle(r) 
print("Area of the circle is: ", c.area())
print("Perimeter of the circle is: ", c.perimeter())
  