import math
class EuclideanDistance:
    def __init__(self):
        self.dist = 0

    def calculate(self, p1, p2):    
        self.dist = math.sqrt( ( (math.pow(p1.x-p2.x, 2)) + (math.pow(p1.y-p2.y, 2)) ) )
        return "The Euclidean Distance between (" + str(p1.x) + ", " + str(p1.y) + ") and (" + str(p2.x) + ", " + str(p2.y) + ") is " + str(self.dist) + "!"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = Point(10, 10)
b = Point(5, 5)

ec = EuclideanDistance()
dist = ec.calculate(a,b)
print(dist)
