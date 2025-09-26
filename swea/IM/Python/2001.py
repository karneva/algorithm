# SWEA 2001 파리퇴치

def kill_fly(flies):
    max_kill = 0
    # 파리채가 덮을 수 있는 공간은 영역 안쪽만 가능
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(M):
                # 한줄 전체의 총 합을 더한다
                total += sum(flies[i+k][j:j+M])

            if total > max_kill:
                max_kill = total
    return max_kill

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t}', kill_fly(flies))