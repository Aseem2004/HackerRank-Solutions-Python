import re

x=re.findall(r"(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])", input())
print(*x if x else [-1], sep="\n")
