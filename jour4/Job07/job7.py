L = [8, 24, 48, 2, 16]
n = 0

for p in range(len(L)):
    if L[p] % 3 == 0:
        n = n + 1

print(n)
