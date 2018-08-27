import math
class Point:
    def __init__(self, x=None, y=None):
        if (x == None):
            self.m_x = 0.0
            self.m_y = 0.0
        elif (y == None):
            self.m_x = x
            self.m_x = y
        else:
            self.m_x = x
            self.m_y = y
    def X(self, new_x = None):
        if (new_x == None):
            return self.m_x
        else:
            self.m_x = new_x
    def Y(self, new_y = None):
        if (new_y == None):
            return self.m_y
        else:
            self.m_y = new_y
    def Distance(self,Point):
        return math.sqrt((self.m_x - Point.m_x)**2 + (self.m_y-Point.m_y) ** 2)

class Line:
    def __init__(self, P1=Point(), P2=Point()):
        self.m_P1 = P1
        self.m_P2 = P2
    def Length(self):
        return (self.m_P1.Distance(self.m_P2))
        
my_Point = Point(3.0, 4.0)
Origin = Point()

my_Line = Line(my_Point)

print(my_Line.Length())

my_Point.X(10.0)
print(my_Point.X())
