import math
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def show(self):
        return self.x,self.y

    def move(self, x1, y1):
        self.x += x1
        self.y += y1

    def dist(self, dis):
        disx=math.sqrt((dis.x-self.x)*(dis.x-self.x))
        disy=math.sqrt((dis.y-self.y)*(dis.y-self.y))
        return disx,disy
p1=Point(int(input()),int(input()))
p2=Point(int(input()),int(input()))
print(p1.show())
p1.move(p2.x,p2.y)
print(p1.show())
print(p1.dist(p2))