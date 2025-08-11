l, c = map(int, input().split())
a, b= map(int, input().split())
a -= 1
b -= 1
mat = []
last_a = []
last_b = []
last_axis = ''
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
        update = False
        if up:
            if mat[a - 1][b] == 1 and a - 1 != last_a:
                last_a.append(a)
                a -=1
                last_axis = 'a'
                update = True
        if down:
            if mat[a + 1][b] == 1 and a + 1 != last_a:
                last_a.append(a)
                a += 1
                last_axis = 'a'
                update = True
        if left:
            if mat[a][b - 1] == 1 and b - 1 != last_b:
                last_b.append(b)
                b -= 1
                last_axis = 'b'
                update = True
        if right:
            if mat[a][b + 1] == 1 and b + 1 != last_b:
                last_b.append(b)
                b += 1
                last_axis = 'b'
                update = True
        if update == False:
            if last_axis == 'a':
                mat[a][b] = 0
                a = last_a[len(last_a) - 1]    
            if last_axis == 'b':
                mat[a][b] = 0
                b = last_b[len(last_b) - 1]       
        
a += 1
b += 1
print(a, b)
