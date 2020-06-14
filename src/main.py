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
        return circleFunc(center, radius + math.sin(p.x/70) * variance + math.cos(p.y / 100) * variance, p)
    return foo


def plane(p):
    x = p.x
    y = p.y

    return x - y

def main():
    win = GraphWin("Window", 700, 700)
    
    #func = plane
    func = circle(Point(350,350), 150)
    #func = wigglyCircle(Point(350, 350), 150, 50)

    cell = Cell(Point(100,100), Point(600, 100), Point(600,600), Point(100,600), EdgeStore(func))
    cell.splitForFunc(func, 0, 5, 1)
    cell.draw(win)

    win.getMouse()

main()