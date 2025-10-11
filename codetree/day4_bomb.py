# codetree 1차원 폭발 게임

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

while True:
    n = len(arr)
    if n == 0:
        break

    remove = [False] * n
    i = 0
    exploded = False

    while i < n:
        j = i + 1
        while j < n and arr[j] == arr[i]:
            j += 1
        if j - i >= M:
            for k in range(i, j):
                remove[k] = True
            exploded = True
        i = j

    if not exploded:
        break

    arr = [arr[i] for i in range(n) if not remove[i]]

print(len(arr))
for v in arr:
    print(v)

'''
input
4 2
1
2
2
1
output
0

input
4 2
1
2
2
3
output
2
1
3

input
8 2
1
3
3
3
2
1
1
2
output
1
1
'''