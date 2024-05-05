import numpy

n=int(input())

x=[list(map(int,input().split())) for i in range(2*n)]
a=x[:n]
b=x[-n:]

print(numpy.dot(a,b))

