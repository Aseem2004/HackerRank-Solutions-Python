from itertools import combinations_with_replacement

s = input().split()
string = sorted(s[0])
number = int(s[1])

ls = list(combinations_with_replacement(string, number))
for i in ls:
    print("".join(i))
