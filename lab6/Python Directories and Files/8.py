import os 
def delete(path):
    if os.access(path,os.X_OK):
        os.remove(path)
    else:
        print("NO PATH")
p=input()
delete(p)