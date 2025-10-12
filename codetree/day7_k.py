# codetree K개 중에 1개를 N번 뽑기

def recur(K, N, path):
    if len(path) == N:
        print(*path)
        return

    for i in range(1, K+1):
        path.append(i)
        recur(K, N, path)
        path.pop()


if __name__ == "__main__":
    K, N = map(int, input().split())
    path = []
    recur(K, N, path)

'''
input
2 2
output
1 1
1 2
2 1
2 2

input
3 2
output
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
'''