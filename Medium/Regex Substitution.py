import re

n=int(input())

for i in range(n):
    x=input()
    x=re.sub(r"(?<=\s)(&&)(?=\s)", r"and",x)
    x=re.sub(r"(?<=\s)(\|\|)(?=\s)", r"or",x)
    print(x)