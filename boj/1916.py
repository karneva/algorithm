# 백준 1916번: 최소비용 구하기
import sys
import heapq

def dijkstra(start, end):
    dist = [10**18] * (N+1)
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

    return dist[end]

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

print(dijkstra(start, end))