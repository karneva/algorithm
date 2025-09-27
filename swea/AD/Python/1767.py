# SWEA 1767 프로세서 연결하기

def field(array, total, done):
    global result, tmp
 
    # 현재 놓은 코어 개수가 기존에 완성한 코어 개수와 일치한다면 더 적은 개수의 전선 개수 저장
    if done == tmp:
        result = min(result, total)
    # 현재 놓은 코어가 기존 완성한 코어 개수보다 많다면 전선 개수, 코어 개수 업데이트
    elif done > tmp:
        result = total
        tmp = done
 
    for i, j in core_lst:
        # 아직 놓이 않은 코어만
        if not array[i][j]:
            array[i][j] = True
            for di, dj in delta:
                dfs_completed = [col[:] for col in array]
                ni, nj = i, j
                cnt = 0
                while True:
                    ni += di
                    nj += dj
                    # 전선을 놓을 위치가 끝에 도달하면
                    if 0 > ni or N <= ni or 0 > nj or N <= nj:
                        # 현재 놓은 필드 그대로 재귀
                        field(dfs_completed, total+cnt, done+1)
                        break
                    # 전선이나 코어를 ㅏ만나면 중지
                    if dfs_completed[ni][nj] or processor[ni][nj] == 1:
                        break
                    # 빈 자리에 전선을 놓으며 개수 증가
                    dfs_completed[ni][nj] = True
                    cnt += 1
 
T = int(input())
 
for t in range(1, T+1):
    N = int(input())
    processor = [list(map(int, input().split())) for _ in range(N)]
    # 코어가 놓인 위치와 전선이 놓인 부분을 체크할 리스트
    completed = [[False]*N for _ in range(N)]
 
    core_lst = []
    done = 0
    for i in range(N):
        for j in range(N):
            if processor[i][j] == 1:
                # 테두리에 있는 부분은 더 이상 무언가를 할 필요가 없다
                if i == 0 or j == 0 or i == N-1 or j == N-1:
                    completed[i][j] = True
                    # 이미 완성한 코어 개수
                    done += 1
                # 코어 위치 모으기
                core_lst.append((i, j))
 
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
 
    # 놓인 전선의 개수
    result = 1000000001
    # 완성한 코어의 개수
    tmp = 0
 
    field(completed, 0, done)
 
    print(f'#{t}', result)