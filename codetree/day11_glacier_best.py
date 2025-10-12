# codetree 빙하 시간복잡도 제일 좋은 코드

from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 4방향
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# visited[r][c] == 1 이면 "바깥 공기 BFS 과정에서 이미 본 칸"
# ※ 절대 리셋하지 않음! 각 칸은 최대 1번만 방문 처리 → 전체 O(n*m)
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1  # (0,0)은 바깥 공기

# 초기 바깥 공기 큐
q = deque([(0, 0)])

time = 0        # 경과 시간(라운드 수)
last = 0        # 직전 라운드에서 녹은 치즈 개수

while True:
    # 이번 라운드에 녹일 치즈 후보
    nxt = deque()

    # 바깥 공기 영역을 확장하면서, 공기와 맞닿아 있는 치즈를 nxt에 수집
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if visited[nr][nc]:
                continue
            if a[nr][nc]:         # 치즈(>0)
                nxt.append((nr, nc))  # → 이번 시간에 녹일 대상
            else:                 # 공기(=0)
                q.append((nr, nc))    # → 바깥 공기로 확정, 계속 확장
            visited[nr][nc] = 1

    # 더 이상 녹일 치즈가 없으면 종료
    if not nxt:
        print(time, last)
        break

    # 이번 라운드에서 녹는 치즈를 동시에 녹임
    last = len(nxt)
    for r, c in nxt:
        a[r][c] = 0

    # 방금 녹은 칸들은 이제 공기이므로, 다음 라운드의 시작 큐가 됨
    q = nxt
    time += 1

'''
input
3 3
0 0 0
0 1 0
0 0 0
output
1 1

input
6 7
0 0 0 0 0 0 0
0 1 1 1 1 0 0
0 1 1 0 1 1 0
0 1 0 1 1 1 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0
output
2 4
'''