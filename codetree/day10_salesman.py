# codetree 외판원 순회

def solve(idx, cost, cnt):
    global result

    if cnt == N:
        if field[idx][0] != 0:
            result = min(result, cost + field[idx][0])
        return

    for e in range(1, N):
        if used[e]:
            continue
        w = field[idx][e]
        if w == 0:
            continue

        next_cost = cost + w
        if next_cost >= result:
            continue

        used[e] = True
        solve(e, next_cost, cnt + 1)
        used[e] = False

N = int(input().strip())
field = [list(map(int, input().split())) for _ in range(N)]

INF = 10**18
result = INF
used = [False] * N
used[0] = True

solve(0, 0, 1)
print(result if result != INF else -1)

'''
input
4
0 2 5 9
3 0 8 11
7 3 0 10
9 5 7 0
output
22

input
5
0 5 0 4 4 
5 0 8 8 8 
1 0 0 9 9 
3 8 8 0 6 
3 8 10 6 0 
output
27

input
3
0 7 1 
0 0 9 
8 5 0 
output
24
'''