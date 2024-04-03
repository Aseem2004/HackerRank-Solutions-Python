import re

x,y=map(int,input().split())
n=[list(input()) for i in range(x)]
s="".join(["".join(col) for col in zip(*n)])
print(re.sub(r"(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])", " ",s))