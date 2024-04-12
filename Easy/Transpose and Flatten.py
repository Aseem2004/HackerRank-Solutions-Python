import numpy

n,m=map(int,input().split())

x=[]
y=0

for i in range(n):
    if y<m:
        val=list(map(int,input().split()))
        x.append(val)

array=numpy.array(x)     

print(numpy.transpose(array))        
print(array.flatten())