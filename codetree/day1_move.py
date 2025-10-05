# codetree 방향에 맞춰 이동

n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

x, y = 0, 0

for num in range(n):
    if dir[num] == 'N':
        for _ in range(dist[num]):
            y += 1
    elif dir[num] == 'W':
        for _ in range(dist[num]):
            x -= 1
    elif dir[num] == 'S':
        for _ in range(dist[num]):
            y -= 1
    elif dir[num] == 'E':
        for _ in range(dist[num]): 
            x += 1

print(x, y)

'''
input
4
N 3
E 2
S 1
E 2
output
4 2
'''