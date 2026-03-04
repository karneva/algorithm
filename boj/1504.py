# 백준 1504번: 특정한 최단 경로
import sys
import heapq

def dijkstra(start):
    dist = [10 ** 18] * (N + 1) 
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        cur_dist, now = heapq.heappop(pq)
        if cur_dist != dist[now]:
            continue

        for nxt, w in graph[now]:
            nxt_dist = cur_dist + w
            if nxt_dist < dist[nxt]:
                dist[nxt] = nxt_dist
                heapq.heappush(pq, (nxt_dist, nxt))

    return dist

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

v1, v2 = map(int, input().split())

dist1 = dijkstra(1)
distv1 = dijkstra(v1)
distv2 = dijkstra(v2)

ans = min(dist1[v1]+distv1[v2]+distv2[N], dist1[v2]+distv1[N]+distv2[v1])

if ans >= 10**18:
    print(-1)
else:
    print(ans)
