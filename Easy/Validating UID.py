import re

for i in range(int(input())):
    uid=input()
    count=False
    
    upper=len(re.findall(r"[A-Z]",uid))
    num=len(re.findall(r"[0-9]",uid))
    alpuid=len(set(re.findall(r"[A-Za-z0-9]",uid)))
    
    for i in uid:
        if uid.count(i)>1:
            count= True
            
    if upper>=2 and num>=3 and alpuid==10 and not count:
        print("Valid")
        
    else: 
        print("Invalid")