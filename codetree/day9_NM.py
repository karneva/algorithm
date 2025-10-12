# codetree N개 중에 M개 뽑기

def recur(N, M, path, used):
    if len(path) == M:
        print(*path)
        return

    for i in range(1, N+1):
        if used[i]:
            continue
        if path and i < path[-1]:
            continue
        used[i] = True
        path.append(i)
        recur(N, M, path, used)
        used[i] = False
        path.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    used = [False]*(N+1)
    path = []
    recur(N, M, path, used)

'''
input
3 2
output
1 2
1 3
2 3

input
4 3
output
1 2 3
1 2 4
1 3 4
2 3 4
'''