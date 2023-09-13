# 현수 위치 r,c
# 직사각형 경계선 까지 가는 최솟값
# w-r, r, h-c, c 네가지 값중에 최솟값

import sys
input = sys.stdin.readline

r, c, w, h = map(int, input().rstrip().split())

print(min(r, c, w-r, h-c))