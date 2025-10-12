# codetree 방향에 맞춰 최대로 움직이기

def solve():
    n = int(input().strip())
    num = [list(map(int, input().split())) for _ in range(n)]
    direc = [list(map(int, input().split())) for _ in range(n)]
    r, c = map(int, input().split())

    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0,  0,  1, 1, 1, 0, -1,-1, -1]

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n

    dp = [[-1] * n for _ in range(n)]

    def dfs(x, y):
        if dp[x][y] != -1:
            return dp[x][y]

        d = direc[x][y]
        best = 0
        k = 1
        while True:
            nx, ny = x + dx[d] * k, y + dy[d] * k
            if not in_range(nx, ny):
                break
            if num[nx][ny] > num[x][y]:
                best = max(best, 1 + dfs(nx, ny))
            k += 1

        dp[x][y] = best
        return best

    print(dfs(r - 1, c - 1))

if __name__ == "__main__":
    solve()


'''
input
3
7 1 4
2 6 3
9 8 5
5 3 1
6 3 7
2 4 8
3 3
output
2

input
3
2 8 9
6 4 5
3 7 1
5 3 1
6 3 7
2 4 8
3 3
output
5
'''