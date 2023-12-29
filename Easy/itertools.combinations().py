from itertools import combinations
x = input().split()

for i in range(1,int(x[1]) + 1):
    comms = []
    comms.extend(combinations(sorted(x[0]),i))
    for c in comms:
        print("".join(c))