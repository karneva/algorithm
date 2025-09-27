# SWEA 1767 프로세서 연결하기 GPT가 수정해준 부분

def field(idx, connected, wire_len):
    global result, max_connected

    # 모든 코어를 처리한 경우
    if idx == len(core_lst):
        # 더 많은 코어를 연결한 경우 우선
        if connected > max_connected:
            max_connected = connected
            result = wire_len
        # 같은 개수의 코어라면 전선 길이 최소값 갱신
        elif connected == max_connected:
            result = min(result, wire_len)
        return

    x, y = core_lst[idx]

    for dx, dy in delta:
        nx, ny = x, y
        path = []

        # 전선을 놓을 수 있는지 확인
        while True:
            nx += dx
            ny += dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                # 전선을 실제로 놓고 재귀 호출
                for px, py in path:
                    completed[px][py] = True
                field(idx + 1, connected + 1, wire_len + len(path))
                # 백트래킹
                for px, py in path:
                    completed[px][py] = False
                break
            if completed[nx][ny] or processor[nx][ny] == 1:
                break
            path.append((nx, ny))

    # 전선을 놓지 않는 경우도 고려 (코어 연결 포기)
    field(idx + 1, connected, wire_len)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    processor = [list(map(int, input().split())) for _ in range(N)]
    completed = [[False] * N for _ in range(N)]
    core_lst = []

    # 이미 테두리에 있는 코어는 자동 연결된 것으로 간주
    for i in range(N):
        for j in range(N):
            if processor[i][j] == 1:
                if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                    completed[i][j] = True  # 이미 연결됨
                else:
                    core_lst.append((i, j))  # 연결 시도할 코어만 저장

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    result = float('inf')   # 최소 전선 길이
    max_connected = 0       # 최대 연결 코어 수

    field(0, 0, 0)

    print(f'#{t} {result}')