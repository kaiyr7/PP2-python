s=input()
r=""
for i in reversed(s):
    r+=i
if r==s:
    print("Palindrome")
else:
    print("Not Palindrome")