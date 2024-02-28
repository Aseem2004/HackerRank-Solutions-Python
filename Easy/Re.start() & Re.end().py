import re
s=str(input())
k=str(input())
n=re.compile(r'(?=('+k+'))')
x=list(n.finditer(s))

if not x:
    print((-1,-1))
else:
    for i in x:
        print((i.start(1),i.end(1)-1))
        