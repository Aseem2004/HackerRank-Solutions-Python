import numpy as np

x=int(input())
l=[]

for i in range (x):
    row=list(map(float,input().split()))
    l.append(row)

print(round(np.linalg.det(l),2))
