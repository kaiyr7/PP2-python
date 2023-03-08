import os
os.chdir('/Users/Kaiyr/Documents/python/Lab1/lab6')
l = [] 
for i in range(65,91):
    l.append(chr(i))
for i in l:
    w=i+".txt"
    with open(w,'w') as file:
        file.write(w)