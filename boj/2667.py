# 백준 2667번: 단지번호붙이기

def dfs(x, y):
    stack = [(x, y)]
    field[x][y] = 0
    cnt = 1
    while stack:
        sx, sy = stack.pop()

        for dx, dy in delta:
            nx, ny = sx+dx, sy+dy
            if 0 <= nx < N and 0 <= ny < N:
                if field[nx][ny] == 1:
                    field[nx][ny] = 0
                    stack.append((nx, ny))
                    cnt += 1

    return cnt


N = int(input())

field = [list(map(int, input().strip())) for _ in range(N)]

delta = [(1,0), (0,1), (-1,0), (0,-1)]

# dfs로 돌면서 0으로 만들고 개수를 세서 리스트에 넣기

result = []

for i in range(N):
    for j in range(N):
        if field[i][j] == 1:
            cnt = dfs(i, j)
            result.append(cnt)

result.sort()

l = len(result)
print(len(result))
for x in result:
    print(x)