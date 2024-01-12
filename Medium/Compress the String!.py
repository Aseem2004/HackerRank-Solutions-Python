from itertools import groupby as gb
S = input()
for key,repeater in gb(S):
    tupl = '('+str(len(list(repeater)))+','+' '+ str(key)+')'
    print(tupl,end = ' ')