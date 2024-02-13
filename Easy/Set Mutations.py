x=int(input())
a=set(map(int,input().split()))
y=int(input())
for i in range(y):
    n=input().split()
    
    if n[0]=='update':
        b=set(map(int,input().split()))
        a.update(b)
    
    if n[0]=='intersection_update':
        b=set(map(int,input().split()))
        a.intersection_update(b)
    
    if n[0]=='difference_update':
        b=set(map(int,input().split()))
        a.difference_update(b)
    
    if n[0]=='symmetric_difference_update':
        b=set(map(int,input().split()))
        a.symmetric_difference_update(b)
  
print(sum(a))