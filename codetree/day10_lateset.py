# codetree 가장 오래 걸리는 학생 2

import heapq

def dijkstra(start, adj_list):
    INF = float('inf')
    distance = [INF] * (V + 1)
    distance[start] = 0
    distance[0] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cost, now = heapq.heappop(pq)

        if cost > distance[now]:
            continue

        for nxt, w in adj_list[now]:
            new_cost = cost + w
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))

    return distance

V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]

adj_list = [[] for _ in range(V+1)]

for s, e, v in edges:
    adj_list[e].append((s, v))

dist = dijkstra(V, adj_list)

print(max(dist))

'''
input
5 6
2 1 1
1 5 2
4 5 100
4 2 9
3 2 3
4 3 5
output
11
'''