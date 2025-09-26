import sys
sys.stdin = open('input.txt')

def game(board, k, nums, idx, move):
    global cnt
    if idx >= len(board):
        cnt += 1
        return

    if move == len(nums):
        return

    game(board, k, nums, idx+1, )

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))
    board = [i for i in range(1, m+1)]

    cnt = 0
    game(board, k, nums, 0, 0)