t=int(input())
for i in range(t):
    a=int(input())
    x=set(input().split())
    b=int(input())
    y=set(input().split())
        
    if x.issubset(y)== True:
            print("True")
    else:
            print("False")
