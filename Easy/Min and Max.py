import numpy as np

n,m=map(int,input().split())

l=[]

for i in range(n): 
     l.append(list(map(int,input().split())))

arr=np.array(l) 
print(np.max(np.min(arr,axis=1)))