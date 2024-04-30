import numpy

n,m= map(int,input().split(' '))

x=[numpy.array((input().split(' ')),dtype='int') for i in range(n)]
y=[numpy.array((input().split(' ')),dtype='int') for j in range(n)]
    
print(numpy.add(x,y))
print(numpy.subtract(x,y))
print(numpy.multiply(x,y))
print(numpy.floor_divide(x,y))
print(numpy.mod(x,y))
print(numpy.power(x,y))