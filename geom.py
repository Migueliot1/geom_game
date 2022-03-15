import math
from random import randint
import turtle

# class Point contains x and y coordinates
class Point:

    # create an instance from x and y coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # comparing if points have identical coordinates
    def compare(self, point):
        if type(point) != Point:
            return None
        
        if self.x == point.x and self.y == point.y:
            return True

        return False

    # showing coordinates of a point
    def show_coords(self):
        print('x:', self.x)
        print('y:', self.y)

    # checking if a point is inside given rectangle instance or on its edge
    def falls_in_rectangle(self, rectangle):

        if type(rectangle) != Rectangle:
            return None

        if rectangle.point1.x <= self.x <= rectangle.point2.x \
        and rectangle.point1.y <= self.y <= rectangle.point2.y:
            return True
        else:
            return False

    # finding a distance from the given coordinates
    def distance_from_point(self, x, y):
        # basically finding a hypotenuse of a triangle created by two points
        side1 = self.x - x
        side2 = self.y - y
        hyp = math.sqrt(side1 ** 2 + side2 ** 2)

        return hyp


class Rectangle:

    # initialize a rectangle from two class Points instances
    def __init__(self, point1, point2):
        
        if type(point1) != Point and type(point2) != Point:
            point1 = Point(0, 0)
            point2 = Point(0, 0)
        
        self.point1 = point1
        self.point2 = point2

    # checking if an instance was created with bad parameters or not
    def is_defect(self):

        if self.point1.compare(Point(0, 0)) and self.point2.compare(Point(0, 0)):
            return True
        else:
            return False

    # calculating area of the rectangle
    def area(self):
        
        if self.is_defect():
            return None
        
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


# Rectangle child class which can draw rectangles on a canvas
class GuiRectangle(Rectangle):

    def draw(self, canvas):
        
        if type(canvas) != turtle.Turtle:
            return
        
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()

        # Moving to second point
        canvas.goto(self.point2.x, self.point1.y)
        canvas.goto(self.point2.x, self.point2.y)
        canvas.goto(self.point1.x, self.point2.y)
        canvas.goto(self.point1.x, self.point1.y)


    def showPoint(self, point, canvas):
        if type(canvas) != turtle.Turtle and type(point) != Point:
            return
        
        canvas.penup()
        canvas.goto(point.x, point.y)
        canvas.pendown()


# DEBUG
# Create rectangle object
# rectangle = Rectangle(Point(randint(0, 400), randint(0, 400)),
#                     Point(randint(10, 400), randint(10, 400)))

# # Print rectangle object
# print("Rectangle Coordinates: ",
#     rectangle.point1.x, ",",
#     rectangle.point1.y, "and",
#     rectangle.point2.x, ",",
#     rectangle.point2.y)

# Get point and an area from user
user_x = float(input('Guess x: '))
user_y = float(input('Guess y: '))
user_point = Point(user_x, user_y)

# user_area = float(input('Guess rectangle area: '))

# # Print out the game result
# print('Your point was inside rectangle:', user_point.falls_in_rectangle(rectangle))
# print('Your area was off by:', rectangle.area() -  user_area)

gui = GuiRectangle(Point(randint(0, 400), randint(0, 400)),
                Point(randint(10, 400), randint(10, 400)))
myturtle = turtle.Turtle()
gui.draw(myturtle)
gui.showPoint(user_point, myturtle)
turtle.done()