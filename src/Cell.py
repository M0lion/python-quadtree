from graphics import *

class Cell:
    solid = False

    def __init__(self, a, b, c, d, edgeStore):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.edgeStore = edgeStore

    def splitForFunc(self, func, depth, maxDepth, minDepth = 0):
        a = func(self.a) > 0
        b = func(self.b) > 0
        c = func(self.c) > 0
        d = func(self.d) > 0

        self.aVal = a
        self.bVal = b
        self.cVal = c
        self.dVal = d

        self.addEdges()

        if(depth > maxDepth):
            return

        shouldSplit = False

        if(a != b):
            shouldSplit = True
        elif(b != c):
            shouldSplit = True
        elif(c != d):
            shouldSplit = True
        elif(d != a):
            shouldSplit = True
            
        if(shouldSplit or depth < minDepth):
            self.split()
            for child in self.children:
                child.splitForFunc(func, depth + 1, maxDepth)
        else:
            self.solid = a

    def draw(self, window):
        if(hasattr(self, "children")):
            for child in self.children:
                child.draw(window)
        else:
            rect = Rectangle(self.a, self.c)
            if(self.solid):
                rect.setFill('black')
                rect.setOutline('white')
            else:
                rect.setFill('white')
                rect.setOutline('black')

            rect.draw(window)

            if(False):
                self.drawPoint(self.a, self.aVal).draw(window)
                self.drawPoint(self.b, self.bVal).draw(window)
                self.drawPoint(self.c, self.cVal).draw(window)
                self.drawPoint(self.d, self.dVal).draw(window)
            
            for a in self.edges:
                for b in self.edges:
                    if(not a.isSameEdge(b.a, b.b)):
                        line = Line(a.midpoint, b.midpoint)
                        line.setFill('blue')
                        line.setWidth(5)
                        line.draw(window)

    def drawPoint(self, p, val):
        c = Circle(p, 5)
        if(val):
            c.setFill('black')
            c.setOutline('white')
        else:
            c.setFill('white')
            c.setOutline('black')
        return c

    def halfWay(self, a, b):
        return Point(a.x + (b.x - a.x) / 2, a.y + (b.y - a.y) / 2)

    def split(self):
        self.children = []

        a = self.a
        b = self.b
        c = self.c
        d = self.d

        ab = self.halfWay(a, b)
        bc = self.halfWay(b, c)
        cd = self.halfWay(c, d)
        da = self.halfWay(d, a)
        center = self.halfWay(a, c)

        self.children.append(Cell(a, ab, center, da, self.edgeStore))
        self.children.append(Cell(ab, b, bc, center, self.edgeStore))
        self.children.append(Cell(center, bc, c, cd, self.edgeStore))
        self.children.append(Cell(da, center, cd, d, self.edgeStore))

    def addEdges(self):
        self.edges = []
        if(self.aVal != self.bVal):
            self.edges.append(self.edgeStore.getEdge(self.a, self.b))
        if(self.bVal != self.cVal):
            self.edges.append(self.edgeStore.getEdge(self.b, self.c))
        if(self.cVal != self.dVal):
            self.edges.append(self.edgeStore.getEdge(self.c, self.d))
        if(self.dVal != self.aVal):
            self.edges.append(self.edgeStore.getEdge(self.d, self.a))

        for edge in self.edges:
            edge.rects.append(self)


