k=int(input())
l=list(map(int, input().split()))

s=set(l)

for i in s:
    if i in l:
        l.remove(i)

for i in s:
    if i not in l:
        print(i)