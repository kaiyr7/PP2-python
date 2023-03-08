import os
os.chdir('/Users/Kaiyr/Documents/python/Lab1/lab6')
r= open("samp.txt",'r')
w= open("sample.txt",'w')
for i in r:
    w.write(i.__str__())