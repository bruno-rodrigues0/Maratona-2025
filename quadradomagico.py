n = int(input())
square, values = [], []
d1, d2 = 0, 0
is_magic = True
for i in range (n):
    square.append(list(map(int, input().split())))
for i in range(len(square)):
    values.append(sum(square[i]))
    tmp_sum = 0
    for j in range(len(square)):
        tmp_sum += square[j][i]
    values.append(tmp_sum)
    d1 += square[i][i]
    d2 += square[i][(len(square[0]) - 1) - i]
values.append(d1)
values.append(d2)
for k in values:
    if k != values[0]:
        is_magic = False
print(values[0] if is_magic else -1)

