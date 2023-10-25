if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [('.|.'*_n).center(m,'-') for _n in range(1,n, 2)]
    print('\n'.join(arr + ["WELCOME".center(m,'-')] + list(reversed(arr))))