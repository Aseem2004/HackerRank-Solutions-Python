import numpy 

n,m = map(int, input().split()) 
x=[numpy.array(input().split(),dtype=int) for i in range(n)] 

print(numpy.sum(x,axis=0).prod())