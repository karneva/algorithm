# 백준 2667번: 단지번호붙이기

import sys
sys.stdin = open("input.txt")

N = int(input())

filed = [list(map(int, input())) for i in range(N)]

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

