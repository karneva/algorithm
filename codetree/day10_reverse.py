# codetree 거꾸로 순열

def recur(n, path, used):
    if len(path) == n:
        print(*path)
        return

    for i in range(n, 0, -1):
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        recur(n, path, used)
        used[i] = False
        path.pop()


if __name__ == "__main__":
    n = int(input())

    path = []
    used = [False] * (n+1)
    recur(n, path, used)

'''
input
3
output
3 2 1
3 1 2
2 3 1
2 1 3
1 3 2
1 2 3
'''
