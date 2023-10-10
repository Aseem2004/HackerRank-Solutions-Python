if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    i = 0
    j = 0
    k = 0
    lis1=[]
    while i<=x:
        while j<=y:
            while k<=z:
                lis=[i,j,k]
                if (i+j+k)!=n:
                    lis1.append(lis)
                    
                k+=1
            j+=1
            k=0
        i+=1
        j=0
    print(lis1)
