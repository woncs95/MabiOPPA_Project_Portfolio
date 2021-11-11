import re

char=[]
b=[56,60,96]
a=[]
lst=[]
print(len(b))
print(list(range(len(b))))
for i in range(len(b)):
    print(i)
    if i == len(b)-i-1:
        a.append(b[i])
    if i < len(b)-i-1:
        print(i)
        a.append(b[i]+b[len(b)-i-1])
        print(a)
    if i<=len(b)-i-1:
        char.append(re.sub(r"[^a-zA-Z0-9]","",chr(a[i]))) ##without nonletter&unlock
        #new_a=list(map(ord,char))
        lst+=char
print(lst)
print(char)
print(list(map(chr, a)))