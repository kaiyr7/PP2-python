import os
#print(os.getcwd())
#os.chdir('/Users/Kaiyr/Documents/python/Lab1/lab6')
def existense(path):
    print(os.access(path, os.F_OK))
def readabilty(path):
    print(os.access(path,os.R_OK))
def writeability(path):
    print(os.access(path,os.W_OK))
def executability(path):
    print(os.access(path,os.X_OK))
p=input()
existense(p)
readabilty(p)
writeability(p)
executability(p)