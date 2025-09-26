import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    Russia = [list(input()) for _ in range(N)]

    white = M - Russia[0].count('W')
    Russia[0] = ['W' for _ in range(M)]
    red = M - Russia[N-1].count('R')
    Russia[N-1] = ['R' for _ in range(M)]

    # 두번째 줄이랑 세번째 줄을 화이트로 할지 블루로 할지 계산
    # 마찬가지로 -2 줄을 레드로 할지 블루로 할지 계산

    i = 1
    while True:
        cnt = 0
        if M - Russia[i].count('W') > M - Russia[i].count('B'):
            pass

    print()