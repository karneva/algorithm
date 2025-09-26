import sys
sys.stdin = open('input.txt')

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

# n: 숫자의 개수, m: 연속해서 m개 이상일 때 폭탄이 터짐.
n, m = tuple(map(int, input().split()))
numbers = [int(input()) for _ in range(n)]


def get_last_idx(idx, num):
    for i in range(idx + 1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            return i - 1

    return len(numbers) - 1


while True:
    explode = False

    for idx in range(len(numbers)):
        num = numbers[idx]

        if num == 0:
            continue

        # 만약 num이 m개 이상 반복된다면
        # 터뜨린다. => numbers[i]=0으로 만들어준다.
        last_idx = get_last_idx(idx, num)

        cnt = last_idx - idx + 1  # 연속되는 개수
        if cnt >= m:
            explode = True
            for i in range(idx, last_idx + 1):
                numbers[i] = 0

    tmp = []
    for i in range(len(numbers)):
        if numbers[i] != 0:
            tmp.append(numbers[i])
    numbers = tmp[::]

    if not explode:
        break

print(len(numbers))
for i in range(len(numbers)):
    print(numbers[i])