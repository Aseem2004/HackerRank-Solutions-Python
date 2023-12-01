from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(1, n+1):
    n_word = input()
    d[n_word].append(i)

for j in range(m):
    m_word = input()
    if d[m_word]:
        print(*d[m_word])
    else:
        print("-1")