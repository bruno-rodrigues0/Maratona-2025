n, k = map(int, input().split())
l = list(map(int, input().split()))
sum = 0
count = 0
i = 0
while i < len(l) - 1:
    if sum == k:
        count += 1
        
    elif sum > k:
        sum = l[i]
        l = l[i:]
        i = 0
        continue
    sum += l[i]
    i += 1
print(count)


