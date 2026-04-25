import turtle
from random import randint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        is_inside = (
            min(rectangle.point1.x, rectangle.point2.x)
            <= self.x
            <= max(rectangle.point1.x, rectangle.point2.x)
        ) and (
            min(rectangle.point1.y, rectangle.point2.y)
            <= self.y
            <= max(rectangle.point1.y, rectangle.point2.y)
        )
        return is_inside


class Rectangle:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        length = self.point2.x - self.point1.x
        height = self.point2.y - self.point1.y
        return abs((length) * (height))


class GUIRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GUIPoint(Point):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(5, "red")


# create a rectangle with random coordinates
rectangle = GUIRectangle(
    Point(randint(-10, 10), randint(-10, 10)), Point(randint(11, 20), randint(11, 20))
)

print(
    f"Rectangle corners: ({rectangle.point1.x}, {rectangle.point1.y}), ({rectangle.point2.x}, {rectangle.point2.y})"
)

# get point and area from user
user_point = GUIPoint(
    int(input("Enter x coordinate: ")), int(input("Enter y coordinate: "))
)
print(
    f"Your point is {'inside' if user_point.falls_in_rectangle(rectangle) else 'outside'} the rectangle."
)
user_area = int(input("Enter area of rectangle: "))
print(
    f"Your rectangle's area is {rectangle.area()}. Your answer is {'correct' if user_area == rectangle.area() else 'incorrect by ' + str(abs(user_area - rectangle.area()))}."
)

myturtle = turtle.Turtle()
rectangle.draw(myturtle)
user_point.draw(myturtle)

turtle.done()
