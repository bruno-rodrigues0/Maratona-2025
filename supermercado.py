n = int(input())
l = []
for i in range(n):
    li = list(map(float, input().split()))
    fator = 1000/li[1]
    l.append(li[0]*fator)
print(f"{min(l):.2f}")
