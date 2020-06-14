from graphics import Point

class Edge:
    def __init__(self, a, b, func):
        self.a = a
        self.b = b
        self.rects = []

        searchA = a
        searchB = b

        base = func(a) > 0

        midpoint = a

        i = 0
        while(i < 5):
            test = Point(searchA.x + (searchB.x - searchA.x) / 2, searchA.y + (searchB.y - searchA.y) / 2)
            testVal = func(test) > 0
            if(testVal == base):
                searchA = test
            else:
                searchB = test

            midpoint = test
            i += 1

        self.midpoint = midpoint

    def isSameEdge(self, a,b):
        if(a.x == self.a.x and a.y == self.a.y and b.x == self.b.x and b.y == self.b.y):
            return True
        if(a.x == self.b.x and a.y == self.b.y and b.x == self.a.x and b.y == self.a.y):
            return True
        
        return False