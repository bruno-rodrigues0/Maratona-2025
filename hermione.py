l, c = map(int, input().split())
a, b= map(int, input().split())
a -= 1
b -= 1
mat = []
last_a = -1
last_b = -1
k = 2
for row in mat:
    k += row.count(1)
for i in range(l):
    mat.append(list(map(int, input().split())))
for _ in range(200):
        right = b + 1 <= c - 1
        left = b - 1 >= 0
        up = a - 1 >= 0
        down = a + 1 <= l - 1
        if up:
            if mat[a - 1][b] == 1 and a - 1 != last_a:
                last_a = a
                last_b = -1
                a -=1
        if down:
            if mat[a + 1][b] == 1 and a + 1 != last_a:
                last_a = a
                last_b = -1
                a += 1
        if left:
            if mat[a][b - 1] == 1 and b - 1 != last_b:
                last_b = b
                last_a = -1
                b -= 1
        if right:
            if mat[a][b + 1] == 1 and b + 1 != last_b:
                last_b = b
                last_a = -1
                b += 1
a += 1
b += 1
print(a, b)
