# SWEA 회문2

def find_palindrome(arr):
    arr_T = [list(col) for col in zip(*arr)]
    # 양쪽 끝부터 들어오면서 검사
    for length in range(100, 2, -1):
        for i in range(100):
            for j in range(100 - length):
                for k in range(length // 2):
                    if arr[i][j + k] != arr[i][j + length - k - 1]:
                        break
                else:
                    return length

                for k in range(length // 2):
                    if arr_T[i][j + k] != arr_T[i][j + length - k - 1]:
                        break
                else:
                    return length

for t in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    print(f'#{t} {find_palindrome(arr)}')