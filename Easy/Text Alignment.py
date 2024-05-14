x=int(input())
y='H'

for i in range(x):
    print((y*i).rjust(x-1)+y+(y*i).ljust(x-1))

for i in range(x+1):
    print((y*x).center(x*2)+(y*x).center(x*6))

for i in range((x+1)//2):
    print((y*x*5).center(x*6))

for i in range(x+1):
    print((y*x).center(x*2)+(y*x).center(x*6))

for i in range(x):
    print(((y*(x-i-1)).rjust(x)+y+(y*(x-i-1)).ljust(x)).rjust(x*6))
