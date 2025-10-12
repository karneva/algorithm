# codetree 벽이 있는 충돌 실험

def solve():
    T = int(input().strip())

    dir_map = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for _ in range(T):
        n, m = map(int, input().split())

        count = [[0]*n for _ in range(n)]
        dird  = [[-1]*n for _ in range(n)]

        for _ in range(m):
            x, y, ch = input().split()
            x, y = int(x)-1, int(y)-1
            count[x][y] = 1
            dird[x][y]  = dir_map[ch]

        def in_range(i, j):
            return 0 <= i < n and 0 <= j < n

        for _ in range(2*n):
            next_cnt = [[0]*n for _ in range(n)]
            next_dir = [[-1]*n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    if count[i][j] != 1:
                        continue
                    d = dird[i][j]
                    ni, nj = i + dx[d], j + dy[d]

                    if in_range(ni, nj):
                        next_cnt[ni][nj] += 1
                        next_dir[ni][nj] = d
                    else:
                        nd = (d + 2) % 4
                        next_cnt[i][j] += 1
                        next_dir[i][j] = nd

            for i in range(n):
                for j in range(n):
                    if next_cnt[i][j] >= 2:
                        next_cnt[i][j] = 0
                        next_dir[i][j] = -1

            count, dird = next_cnt, next_dir

        ans = sum(sum(row) for row in count)
        print(ans)

if __name__ == "__main__":
    solve()

'''
input
1
4 5
1 2 L
2 3 U
3 1 R
3 4 D
4 2 U
output
1

input
3
2 2
1 1 L
2 2 R
2 2
1 1 D
2 2 R
2 2
1 1 L
1 2 R
output
2
0
2
'''