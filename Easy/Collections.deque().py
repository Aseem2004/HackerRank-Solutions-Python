from collections import deque
n = int(input())
dq = deque()
for _ in range(n):
    line = input().split()
    line += ['']
    eval(f"dq.{line[0]}({line[1]})")
print(*dq)