class Shape():
    def __init__(self):
        pass
    def Area(self):
        return 0
class Rec(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def Rec(self):
        return self.length*self.width
l=int(input())
w=int(input())
A=Rec(l,w)
print(A.Rec()) 