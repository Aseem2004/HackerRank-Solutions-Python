def print_rangoli(size):
    E=list()
    S="abcdefghijklmnopqrstuvwxyz"
    for i in range(0,size):
       S1=S[0:size]
       S2=S1[::-1]
       A=[S2[j] for j in range(size-i)]
       B=("-").join(A+A[::-1][1:])
       E.append(B.center(4*size-3,"-"))
    print("\n".join(E[::-1]+E[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)