# 백준 1753번: 최단경로
import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = 10**18
dist = [INF] * (V + 1)
dist[K] = 0

pq = [(0, K)]

while pq:
    cur_dist, now = heapq.heappop(pq)
    if cur_dist != dist[now]:
        continue

    for nxt, w in graph[now]:
        nd = cur_dist + w
        if nd < dist[nxt]:
            dist[nxt] = nd
            heapq.heappush(pq, (nd, nxt))

for i in range(1, V + 1):
    print(dist[i] if dist[i] != INF else "INF")