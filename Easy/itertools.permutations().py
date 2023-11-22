# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,n=input().split(' ')
n=int(n)
s=list(s)
s.sort()
x=list(permutations(s,n))
for i in x:
    print("".join(i))