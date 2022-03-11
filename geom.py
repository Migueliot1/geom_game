import math

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

        if rectangle.lowleft.x <= self.x <= rectangle.upright.x \
        and rectangle.lowleft.y <= self.y <= rectangle.upright.y:
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
    def __init__(self, lowleft, upright):
        
        if type(lowleft) != Point and type(upright) != Point:
            lowleft = Point(0, 0)
            upright = Point(0, 0)
        
        self.lowleft = lowleft
        self.upright = upright

    # checking if an instance was created with bad parameters or not
    def is_defect(self):

        if self.lowleft.compare(Point(0, 0)) and self.upright.compare(Point(0, 0)):
            return True
        else:
            return False


# DEBUG
point1 = Point(2, 2)
print ('x:', point1.x)
print('y:', point1.y)

point2 = Point(4, 3)
print('distance:', point1.distance_from_point(point2.x, point2.y))

rectanglex = Rectangle(point1, point2)
point_inside = Point(3, 2)
print('point_inside is in rectanglex?', point_inside.falls_in_rectangle(rectanglex))

# trying sanity checks
print(point1.compare(5))
print('point_inside is in rectanglex?', point_inside.falls_in_rectangle(point2))

rectangle_error = Rectangle(0, 0)
print('rectangle_error lowleft x:', rectangle_error.lowleft.x)
print('rectangle_error upright y:', rectangle_error.upright.y)
print('is rectangle_error defect?', rectangle_error.is_defect())
print('is rectanglex defect?', rectanglex.is_defect())