n = int(input())
s = set(map(int, input().split()))
N = int(input())

actions = {
    "remove": s.remove,
    "discard": s.discard,
    "pop": s.pop
}

for _ in range(N):
    command, *item = input().split()
    if command in actions:
        if item:
            actions[command](int(item[0]))
        else:
            actions[command]()
            
print(sum(list(s)))