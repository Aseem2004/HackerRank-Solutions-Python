import itertools

x=list(map(int,input().split()))
n=x[0]
div=x[1]

total=0
y=[]

for n in range(n):
    y.append(list(set(map(int,input().split()[1:]))))

combinations=list(itertools.product(*y))

maximum=-1
for combo in combinations:
    total_squares=sum([number**2 for number in list(combo)])
    modulo=total_squares%div
    if modulo>maximum:
        maximum=modulo
print(maximum)
