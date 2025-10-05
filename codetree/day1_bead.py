# codetree 작은 구슬의 이동

n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dir = 0
if d == 'U':
    dir = 0
elif d == 'R':
    dir = 1
elif d == 'D':
    dir = 2
else:
    dir = 3

i, j = r, c
for _ in range(t):
    ni = i + delta[dir][0]
    nj = j + delta[dir][1]
    if 0 < ni <= n and 0 < nj <= n:
        i, j = ni, nj
    else:
        dir = (dir+2)%4

print(i, j)

'''
input
4 4
1 2 L
output
1 3
'''