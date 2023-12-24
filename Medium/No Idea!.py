happiness = 0
n,m = map(int, input().split())  
happiness_nos = input().split()
A = set(input().split())         
B = set(input().split())         

for i in happiness_nos:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1

print(happiness)