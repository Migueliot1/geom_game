import math

# class Point contains x and y coordinates
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # comparing if points have identical coordinates
    def compare(self, point):
        if self.x != point.x:
            check_x = False
        else:
            check_x = True

        if self.y != point.y:
            check_y = False
        else:
            check_y = True

        if check_x and check_y:
            return True

        return False

    # showing coordinates of a point
    def show_coords(self):
        print('x:', self.x)
        print('y:', self.y)

    # checking if a point is inside given rectangle instance or on its edge
    def falls_in_rectangle(self, rectangle):
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
        self.lowleft = lowleft
        self.upright = upright



# DEBUG
point1 = Point(2, 2)
print ('x:', point1.x)
print('y:', point1.y)

point2 = Point(4, 3)
print('distance:', point1.distance_from_point(point2.x, point2.y))

rectanglex = Rectangle(point1, point2)
point_inside = Point(3, 2)
print('point_inside is in rectanglex?', point_inside.falls_in_rectangle(rectanglex))