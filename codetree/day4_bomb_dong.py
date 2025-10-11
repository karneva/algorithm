# codetree 1차원 폭발 게임 dong 강사님 코드

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

'''
input
4
1 2 4 3
3 2 2 3
3 1 6 2
4 5 4 4
2 3
output
1 0 0 0
3 2 0 3
3 1 0 2
4 5 4 4

input
4
1 2 4 3
3 2 2 3
3 1 6 2
4 5 4 4
3 3
output
0 0 0 0
1 2 0 3
3 2 0 3
4 5 0 4
'''