# codetree 빙하 dong 강사님 코드

from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 4방향
DR = (-1, 0, 1, 0)
DC = (0, 1, 0, -1)

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

# 바깥 물을 (0,0)에서 BFS로 확장하면서
# 인접한 빙하(>0)를 '이번에 녹일 목록'에 모은다.
def collect_to_melt():
    vis = [[False]*m for _ in range(n)]
    q = deque([(0, 0)])
    vis[0][0] = True

    to_melt = set()

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + DR[d], c + DC[d]
            if not in_range(nr, nc) or vis[nr][nc]:
                continue
            if a[nr][nc] == 0:
                # 바깥 물로 확장
                vis[nr][nc] = True
                q.append((nr, nc))
            else:
                # 물과 맞닿은 빙하 → 이번에 녹음
                to_melt.add((nr, nc))
                # 빙하는 큐에 넣지 않음 (한 시간에 바로 물이 되지 않음)
    return to_melt

time = 0
last = 0

while True:
    melt_set = collect_to_melt()
    if not melt_set:              # 더 이상 녹일 빙하가 없음 → 종료
        print(time, last)
        break

    last = len(melt_set)          # 이번에 녹을 빙하 수
    for r, c in melt_set:
        a[r][c] = 0               # 한 시간에 동시에 녹음

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