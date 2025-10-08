# programmers 방문길이

def solution(dirs):
    # 방향 이동, 방문 처리
    delta = {
        'U': (1, 0),
        'D': (-1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }
    direction = ['U', 'L', 'D', 'R']
    visited = set()
    cur_x, cur_y = 0, 0
    
    for dir in dirs:
        nx, ny = cur_x+delta[dir][0], cur_y+delta[dir][1]

        if not (-5<=nx<=5 and -5<=ny<=5):
            continue

        visited.add((nx, ny, direction.index(dir)))
        visited.add((cur_x, cur_y, (direction.index(dir)+2)%4))
        cur_x, cur_y = nx, ny

    return len(visited)/2

if __name__ == "__main__":
    dirs = "LULLLLLLU"
    print(solution(dirs))