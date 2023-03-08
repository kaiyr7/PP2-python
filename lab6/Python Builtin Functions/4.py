import time
a = int(input())
t = int(input())
time.sleep(t/1000)
print(("Square root of {} after {} miliseconds is {}").format(a,t,a**(1/2)))