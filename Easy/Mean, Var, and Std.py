import numpy

n,m=map(int,input().split())

x=[]

for i in range(n):
    arr=list(map(int,input().split()))
    x.append(arr)
    
print(numpy.mean(x,axis=1))
print(numpy.var(x,axis=0))
print(round(numpy.std(x,axis=None),11))