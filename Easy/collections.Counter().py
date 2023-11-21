# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
shoe_lst = [int(x) for x in input().split()]
size_cou = Counter(shoe_lst)
N = int(input())
total = 0

for i in range(N):
    cus = input().split()
    size, price = int(cus[0]), int(cus[1])
    if size_cou[size] > 0:
        total += price
        size_cou[size] -= 1
    
print(total)