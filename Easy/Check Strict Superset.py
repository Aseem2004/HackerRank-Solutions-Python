a=set(map(int,input().split()))
n=int(input())
for i in range(n):
    x=set(map(int,input().split()))
    if not a.issuperset(x):
        print("False")
        break
else:
    print("True")
