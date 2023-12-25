m = input()
a = set(input().split(' '))
n = input()
b = set(input().split(' '))
intersect = sorted(list(map(int,(a-b).union(b-a))))
for i in intersect:
    print(i)