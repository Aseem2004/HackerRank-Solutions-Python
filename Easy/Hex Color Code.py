import re

for i in range(int(input())):
    r=re.findall(r"(?<=.)#[a-fA-F0-9]{3,6}",input())
    if r:
        print(*r,sep="\n")