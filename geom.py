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

# class Rectangle contains 2 points to create a Rectangle from them
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


# Point child class which can draw a point on a canvas
class GuiPoint(Point):

    # Draw a point on a given canvas
    def draw(self, canvas, size=5, color='red'):

        if type(canvas) != turtle.Turtle:
            return
        
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)
