import math
class filterPrime():
    def Prime(self, n):
        if(n<2):
            return False
        else:
            for i in range(2,n):
                if(n%i == 0):
                    return False
        return True
    def Filter(self, listPrime):
        return filter(lambda x: self.Prime(x), listPrime)
v = []
for i in range(5):
    y=int(input())
    v.append(y)
f=filterPrime()
l=list(f.Filter(v))
print(l)