import turtle
from random import randint
from geom import Point, GuiPoint, GuiRectangle

# Create a canvas instance
myturtle = turtle.Turtle()

# Get point and an area from user
er_msg = 'Wrong input. Assigning {} to default value of 0.'
try:
    user_x = float(input('Guess x: '))
except:
    print(er_msg.format('user_x'))
    user_x = 0

try:
    user_y = float(input('Guess y: '))
except:
    print(er_msg.format('user_y'))
    user_y = 0

try:
    user_area = float(input('Guess rectangle area: '))
except:
    print(er_msg.format('user_area'))
    user_area = 0

# Create a point out of user's input and a randomly generated rectangle
user_point = GuiPoint(user_x, user_y)
rand_rect = GuiRectangle(Point(randint(0, 400), randint(0, 400)),
                Point(randint(10, 400), randint(10, 400)))

# Print out the game result
msg = "Rectangle's coordinates: {x1}, {y1} and {x2}, {y2}."

print('***')
print(msg.format(x1=rand_rect.point1.x, y1=rand_rect.point1.y, x2=rand_rect.point2.x, y2=rand_rect.point2.y))
print('Your point was inside rectangle:', user_point.falls_in_rectangle(rand_rect))
print('Your area was off by:', rand_rect.area() -  user_area)
print('***')

# Draw rectangle and point
rand_rect.draw(myturtle)
user_point.draw(myturtle, 10)

turtle.done()