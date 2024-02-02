from itertools import combinations
N = int(input())
letters = input().split()
K = int(input())
combin = list(combinations(letters, K))
contain_a = [tup for tup in combin if 'a' in tup]
print(len(contain_a) / len(combin))