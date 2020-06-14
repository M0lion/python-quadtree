from graphics import *
from Cell import Cell
from EdgeStore import EdgeStore
import math

def circleFunc(center, radius, p):
    x = p.x
    y = p.y

    x -= center.x
    y -= center.y

    distSq = x * x + y * y
    radSq = radius * radius

    return distSq - radSq


def circle(center, radius):
    def foo(p):
        return circleFunc(center, radius, p)
    return foo

def wigglyCircle(center, radius, variance):
    def foo(p):
        return circleFunc(center, radius + math.sin(p.x/70) * variance + math.cos(p.y / 100) * 0, p)
    return foo

def rotate(angle, point, func):
    def foo(p):
        x = p.x
        y = p.y

        x -= point.x
        y -= point.y

        x = x*math.cos(angle) - y*math.sin(angle)
        y = x*math.sin(angle)+y*math.cos(angle)
        
        x += point.x
        y += point.y

        rot = Point(x,y)

        return func(rot)
    return foo

def plane(p):
    x = p.x
    y = p.y

    return x - y

def main():
    win = GraphWin("Window", 700, 700)
    
    #func = plane
    #func = circle(Point(350,350), 150)
    func = wigglyCircle(Point(350, 350), 150, 75)

    func = rotate(45, Point(350, 350), func)

    a = 50
    b = 650

    cell = Cell(Point(a,a), Point(b, a), Point(b,b), Point(a,b), EdgeStore(func))
    cell.splitForFunc(func, 0, 7, 1)
    cell.draw(win)

    win.getMouse()

main()