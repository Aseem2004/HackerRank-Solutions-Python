import numpy

a=numpy.array((input().split()),dtype='int')
b=numpy.array((input().split()),dtype='int')

print(numpy.inner(a,b))
print(numpy.outer(a,b))