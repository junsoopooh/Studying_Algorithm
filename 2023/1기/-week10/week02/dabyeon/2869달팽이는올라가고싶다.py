# 완전히 하루를 카운트 할 수 있는 식 : (V-B) // (A-B)
# (V-B) % (A-B) 가 있는 경우 + 1

import sys
input = sys.stdin.readline

A, B, V = map(int, input().rstrip().split())

if (V-A) % (A-B) != 0:
    print((V-B) // (A-B) + 2)
else:
    print((V-B) // (A-B) + 1)