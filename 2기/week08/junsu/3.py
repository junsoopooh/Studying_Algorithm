# 최솟값 만들기
from heapq import heappop, heappush
def solution(A,B):
    answer = 0
    n = len(A)
    heap_A = []
    heap_B = []
    for i in range(n):
        heappush(heap_A,A[i])
        heappush(heap_B,-1*B[i])
    for i in range(n):
        a = heappop(heap_A)
        b = heappop(heap_B)
        answer += a*b*(-1)
    return answer
