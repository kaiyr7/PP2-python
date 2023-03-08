import os
os.chdir('/Users/Kaiyr/Documents/python/Lab1/lab6')
def dirs():
    for i in os.listdir():
        if os.path.isdir(i):
            print(i)
def files():
    for i in os.listdir():
        if os.path.isfile(i):
            print(i)
def all():
    print(os.listdir())
dirs()
files()
all()