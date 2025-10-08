# programmers 게임 맵 최단거리

from collections import deque

def solution(maps):
    answer = 21e8
    n, m = len(maps), len(maps[0])
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = deque([(0, 0, 1)])

    while queue:
        cur_x, cur_y, d = queue.popleft()

        if cur_x == n-1 and cur_y == m-1:
            answer = min(answer, d)
            continue

        for dx, dy in delta:
            nx, ny = cur_x+dx, cur_y+dy

            if not (0<=nx<n and 0<=ny<m):
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = 0
                queue.append((nx, ny, d+1))

    return answer if answer != 21e8 else -1

if __name__ == "__main__":
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    print(solution(maps))