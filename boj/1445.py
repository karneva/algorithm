# 백준 1445번: 일요일 아침의 데이트
import sys
import heapq

"""
문제 감각

격자에서 S → F로 가는데, 길의 “비용”이 다음처럼 정의됨

쓰레기 칸(g)을 밟으면 1 증가 (이게 1순위로 최소화)

쓰레기 옆 칸(상하좌우가 g인 칸)을 밟으면 1 증가 (이게 2순위로 최소화)

즉 목표는
“쓰레기 밟은 횟수 최소” → 동률이면 “쓰레기 옆 칸 밟은 횟수 최소”

풀이 핵심 (다익스트라)

우선순위 큐에 거리 대신 **(g_cnt, near_cnt, x, y)**를 넣고,
dist도 숫자 하나가 아니라 **쌍(dist_g, dist_near)**로 관리하면 된다.

비교는 파이썬 튜플이 알아서 해줌
(a1, b1) < (a2, b2) 이런 식으로 사전식 비교가 되니까.

입력 받을 때 쓰레기 주변을 미리 체크해두면 그 곳에서 근처에 쓰레기가 있는지 매번 찾을 필요가 없다.
"""

input = sys.stdin.readline

def dijkstra(sx, sy, ex, ey):
    dist = [[(10**18, 10**18, 10**18) for _ in range(M)] for _ in range(N)]

    dist[sx][sy] = (0, 0, 1)

    pq = [(0, 0, 1, sx, sy)]

    while pq:
        g_cnt, near_cnt, cur_dist, x, y = heapq.heappop(pq)

        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M:
                if (g_cnt, near_cnt, cur_dist) > dist[nx][ny]:
                    continue
                if forrest[nx][ny] == 'g':
                    if dist[nx][ny] > (g_cnt+1, near_cnt, cur_dist+1):
                        dist[nx][ny] = (g_cnt+1, near_cnt, cur_dist+1)
                        heapq.heappush(pq, (g_cnt+1, near_cnt, cur_dist+1, nx, ny))
                elif forrest[nx][ny] == 'n':
                    if dist[nx][ny] > (g_cnt, near_cnt+1, cur_dist+1):
                        dist[nx][ny] = (g_cnt, near_cnt+1, cur_dist+1)
                        heapq.heappush(pq, (g_cnt, near_cnt+1, cur_dist+1, nx, ny))
                elif forrest[nx][ny] in ('.', 'F'):
                    if dist[nx][ny] > (g_cnt, near_cnt, cur_dist+1):
                        dist[nx][ny] = (g_cnt, near_cnt, cur_dist+1)
                        heapq.heappush(pq, (g_cnt, near_cnt, cur_dist+1, nx, ny))

    return (dist[ex][ey][0], dist[ex][ey][1])

N, M = map(int, input().split())
forrest = [list(input().rstrip()) for _ in range(N)]

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

sx, sy, ex, ey = 0, 0, 0, 0

for i in range(N):
    for j in range(M):
        if forrest[i][j] == 'S':
            sx, sy = i, j
        elif forrest[i][j] == 'F':
            ex, ey = i, j
        elif forrest[i][j] == 'g':
            for dx, dy in delta:
                nx, ny = i+dx, j+dy

                if 0 <= nx < N and 0 <= ny < M and forrest[nx][ny] not in ('S', 'F', 'g'):
                    forrest[nx][ny] = 'n'

x, y = dijkstra(sx, sy, ex, ey)
print(x, y)
