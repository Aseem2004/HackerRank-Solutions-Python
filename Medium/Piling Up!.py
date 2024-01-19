from collections import deque
ls0=[]
num=int(input())
for x in range(num):
    n=int(input())
    de=deque(map(int, input().split()))
    ls=[]
    while len(de)>1:
        if de[0]<de[-1]:
            ls.append(de[-1])
            de.pop()
        elif de[0]>de[-1]:
            ls.append(de[0])
            de.popleft()
        elif de[0]==de[-1]:
            ls.append(de[-1])
            ls.append(de[0])
            de.pop()
            de.popleft()
    if len(de)==1:
        ls.append(de[0])
    if ls == sorted(ls, reverse=True):
        ls0.append('Yes')
    else:
        ls0.append('No')
for element in ls0:
    print(element)