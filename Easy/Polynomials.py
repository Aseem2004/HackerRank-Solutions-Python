import numpy

p=numpy.array((input().split()),dtype='float')
x=int(input().strip())

print(numpy.polyval(p,x))