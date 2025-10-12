# codetree 강력한 폭발

def solve():
    n = int(input().strip())
    grid = [list(map(int, input().split())) for _ in range(n)]

    # 폭탄을 둘 좌표(= 입력에서 1인 칸 리스트)
    pts = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
    k = len(pts)

    # 폭탄 3종 모양 (중심 포함!)
    B1 = [(-2, 0), (-1, 0), (1, 0), (2, 0)]
    B2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    B3 = [(-1,-1), (1,-1), (-1, 1), ( 1, 1)]
    bombs = [B1, B2, B3]

    def inside(x, y): return 0 <= x < n and 0 <= y < n

    # 전처리: 각 포인트마다 3가지 폭탄형이 덮는 좌표 목록(중심 포함)
    cover = []
    for (r, c) in pts:
        per = []
        for b in bombs:
            cells = [(r, c)]  # 중심 포함
            for di, dj in b:
                ni, nj = r + di, c + dj
                if inside(ni, nj):
                    cells.append((ni, nj))
            per.append(cells)
        cover.append(per)

    # 간단 상한: 폭탄 하나가 최대 5칸(중심+4)을 더 덮을 수 있음
    MAX_PER_BOMB = 5
    seen = [[False]*n for _ in range(n)]
    best = 0

    def dfs(idx: int, cur: int):
        nonlocal best
        # 상한 가지치기
        if cur + (k - idx) * MAX_PER_BOMB <= best:
            return
        if idx == k:
            if cur > best:
                best = cur
            return

        # 현재 포인트에서 3가지 폭탄형만 시도(고정 순서 → 3^K)
        for t in range(3):
            added = []
            for x, y in cover[idx][t]:
                if not seen[x][y]:
                    seen[x][y] = True
                    added.append((x, y))
            dfs(idx + 1, cur + len(added))
            # 되돌리기
            for x, y in added:
                seen[x][y] = False

    dfs(0, 0)
    print(best)

if __name__ == "__main__":
    solve()

'''
input
4
0 0 0 0
0 0 1 0
0 1 0 0
0 0 0 0
output
9

input
4
0 1 0 0
0 1 0 0
0 1 0 0
0 1 0 0
output
12
'''