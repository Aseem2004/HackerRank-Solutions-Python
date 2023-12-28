from collections import OrderedDict
od = OrderedDict()
for _ in range(int(input())):
    *item, price =input().split()
    if ' '.join(item) in od:
        od[' '.join(item)] += int(price)
    else:
        od[' '.join(item)] = int(price)
    
for key, value in od.items():
    print(key, value)
