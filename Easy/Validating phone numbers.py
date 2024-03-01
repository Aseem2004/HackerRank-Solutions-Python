import re

reg=r"^[789]\d{9}$"
for i in range(int(input())):
    s=input()
    r=re.search(reg,s)
    
    if bool(r):
        print("YES")
    else:
        print("NO")