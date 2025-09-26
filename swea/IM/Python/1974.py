# SWEA 1974 스도쿠 검증

def sudoku(arr):
    # 스도쿠인지 검증할 sort 리스트
    is_sudoku = [i for i in range(1, 10)]
    # 전치 행렬
    arr_T = list(zip(*arr))

    # 원행렬과 전치 행렬을 돌면서 정렬된 리스트가 검증 리스트와 일치 하지 않으면 0
    for i in range(9):
        if sorted(arr[i]) != is_sudoku:
            return 0
        if sorted(arr_T[i]) != is_sudoku:
            return 0

    # 9개 블럭의 숫자를 square 리스트에 넣고 스도쿠 검증
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = []
            for k in range(3):
                square.extend(arr[i+k][j:j+3])

            if sorted(square) != is_sudoku:
                return 0
    # 단 한번도 안걸리고 왔다면 1
    return 1

T = int(input())

for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{t}', sudoku(arr))