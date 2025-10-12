# codetree 수들의 합 최대화하기

def recur(cnt, total):
    global result

    if cnt == n:
        result = max(result, total)
        return

    for i in range(n):
        if used[i]:
            continue

        used[i] = True
        recur(cnt + 1, total + grid[cnt][i])
        used[i] = False


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

used = [False] * n
result = 0
recur(0, 0)

print(result)

'''
input
3
3 5 3
5 8 4
2 7 1
output
15
'''