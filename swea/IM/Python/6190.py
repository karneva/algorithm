# SWEA 6190 정곤이의 단조 증가하는 수

def danzo(arr):
    # 먼저 두 수의 곱을 하고 단조인지 아닌지 판단
    # 그 수가 단조라면 변수에 할당
    # 그 다음 곱들이 그 단조보다 작으면 pass
    danzo_num = 0
    for i in range(len(arr)-1, 0, -1):
        for j in range(i-1, -1, -1):
            num = arr[i] * arr[j]
            if num < danzo_num:
                break

            for n in range(len(str(num))-1):
                if str(num)[n] > str(num)[n+1]:
                    break
            else:
                danzo_num = num

    if danzo_num == 0:
        return -1
    else:
        return danzo_num

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(f'#{t}', danzo(arr))
