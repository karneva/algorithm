# codetree 특정 조건에 맞게 K개 중에 1개를 N번 뽑기

def recur(K, N, path):
    if len(path) == N:
        for j in range(1, N-1):
            if path[j-1] == path[j] == path[j+1]:
                return
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
2 1
output
1
2

input
2 3
output
1 1 2
1 2 1
1 2 2
2 1 1
2 1 2
2 2 1
'''