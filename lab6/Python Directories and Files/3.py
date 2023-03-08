import os
def exist(path):
    if os.access(path, os.F_OK):
        for i in os.listdir(path):
            if os.path.isfile(os.path.join(path, i)):
                print(i)
    else:
        print("NO PATH")
p=input()
exist(p)