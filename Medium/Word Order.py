from collections import Counter

n = int(input())
words = [input() for _ in range(n)]
word_count = Counter(words)

print(len(word_count))
print(*word_count.values())