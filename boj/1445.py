# 백준 1445번: 일요일 아침의 데이트
import sys
import heapq

sys.stdin = open('input.txt')

"""
문제 감각

격자에서 S → F로 가는데, 길의 “비용”이 다음처럼 정의됨

쓰레기 칸(g)을 밟으면 1 증가 (이게 1순위로 최소화)

쓰레기 옆 칸(상하좌우가 g인 칸)을 밟으면 1 증가 (이게 2순위로 최소화)

즉 목표는
“쓰레기 밟은 횟수 최소” → 동률이면 “쓰레기 옆 칸 밟은 횟수 최소”

풀이 핵심 (다익스트라)

우선순위 큐에 거리 대신 **(g_cnt, near_cnt, x, y)**를 넣고,
dist도 숫자 하나가 아니라 **쌍(dist_g, dist_near)**로 관리하면 된다.

비교는 파이썬 튜플이 알아서 해줌
(a1, b1) < (a2, b2) 이런 식으로 사전식 비교가 되니까.
"""

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]