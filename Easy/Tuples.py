import random
count = int(input())
elements = input().split()
if len(elements) == count:
  t = tuple([int(x) for x in elements])
  print(hash(t))
