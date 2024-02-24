import re

for i in range(int(input())):
    x=re.search(r"^[+-]?\d*\.\d+$", input())
    print(bool(x))