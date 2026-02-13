# 백준 11724번: 연결 요소의 개수

from collections import deque

def dfs(idx):
    stack = [idx]

    while stack:
        next = stack.pop()

        for i in adj_list[next]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)

def bfs(idx):
    queue = deque([idx])

    while queue:
        next = queue.popleft()

        for i in adj_list[next]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]

# for _ in range(M):
#     u, v = map(int, input().split())
#     adj_list[u].append(v)
#     adj_list[v].append(u)
#
# visited = [False] * (N+1)
# visited[0] = True
#
# cnt = 0
#
# for i in range(1, N+1):
#     if not visited[i]:
#         # dfs(i)
#         bfs(i)
#         cnt += 1
#
# print(cnt)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return
    
    # union by rank
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1

parent = [i for i in range(N+1)]
rank = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

roots = {find(i) for i in range(1, N + 1)}
print(len(roots))