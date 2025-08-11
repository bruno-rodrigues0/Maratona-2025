n, m = map(int, input().split())
for i in range(m, 0, -1):
    if(m // i == 1 and n // i == 1):
        print(i - 1)
        break

