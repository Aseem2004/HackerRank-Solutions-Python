N,M = input(),input().split()
print(all([all(int(i) >= 0 for i in M),any(i == i[::-1] for i in M)]))