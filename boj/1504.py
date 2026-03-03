# 백준 1504번: 특정한 최단 경로
import sys
import heapq

sys.stdin = open("input.txt")

N, E = map(int, input().split())

graph = [[] for _ in range(E+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

v1, v2 = map(int, input().split())

dist1 = [10**18] * (N+1)  # v1, v2 최소 구하고
dist1[1] = 0

pq1 = [(0, 1)]

while pq1:
    cur_dist, now = heapq.heappop(pq1)

    for nxt, w in graph[now]:
        nxt_dist = cur_dist + w
        if nxt_dist < dist1[nxt]:
            dist1[nxt] = nxt_dist
            heapq.heappush(pq1, (nxt_dist, nxt))

distv1 = [10**18] * (N+1)  # 반대 방향으로 최소 구하고
distv2 = [10**18] * (N+1)  # N으로 최소 구하고
