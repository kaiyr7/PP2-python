from math import tanh
n=int(input())
l=int(input())
def areaofpol(n,l):
    return int(n*l*(l/2*tanh(180/n))/2)
print(areaofpol(n,l))
