c1, c2 = list(map(int, input().split())), list(map(int, input().split()))
t1 = c1[1] / c1[2]
t2 = c2[1] / c2[2]
print(c1[0] if t1 < t2 else c2[0])

