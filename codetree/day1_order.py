# codetree 문자에 따른 명령 2

dirs = input()

x, y = 0, 0
delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dir = 0

for d in dirs:
    if d == 'L':
        dir = 3 if dir - 1 < 0 else dir - 1
    elif d == 'R':
        dir = (dir+1) % 4
    else:
        x, y = x + delta[dir][0], y + delta[dir][1]

print(x, y)

'''
input
LF
output
-1 0
'''