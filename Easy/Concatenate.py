import numpy

N,M,P= map(int,input().split(' '))

arr1=[]
arr2=[]
for i in range(N):
    arr1.append(list(map(int,input().split(' '))))

for j in range(M):
    arr2.append(list(map(int,input().split(' '))))

print(numpy.concatenate((numpy.array(arr1),numpy.array(arr2)),axis=0))
