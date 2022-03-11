import math

# class Point contains x and y coordinates
class Point:

    def __init_(self):
        self.x = 0
        self.y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    def show_coords(self):
        print('x:', self.x)
        print('y:', self.y)

    def falls_in_rectangle(self, lowleft_t, upright_t):
        # lowleft_t and upright_t are tuples with (x, y) values
        if lowleft_t[0] < self.x < upright_t[0] \
        and lowleft_t[1] < self.y < upright_t[1]:
            return True
        else:
            return False

    def distance_from_point(self, x, y):
        # basically finding a hypotenuse of a triangle created by two points
        side1 = abs(self.x - x)
        side2 = abs(self.y - y)
        hyp = math.sqrt(side1 ** 2 + side2 ** 2)

        return hyp



# DEBUG
point1 = Point(2, 2)
print ('x:', point1.x)
print('y:', point1.y)

point2 = Point(4, 3)
print('distance:', point1.distance(point2.x, point2.y))