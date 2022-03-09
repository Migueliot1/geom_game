# class Point contains x and y coordinates of a point
from re import X

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

    def show(self):
        print('x:', self.x)
        print('y:', self.y)


# DEBUG
point1 = Point(10, 20)
print ('x:', point1.x)
print('y:', point1.y)