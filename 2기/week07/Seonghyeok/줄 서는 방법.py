from itertools import permutations

def permu(an, k):
    cnt = 0
    for i in permutations(an, len(an)):
        cnt += 1
        if cnt == k:
            return i

def solution(n, k):
    answer = []
    for i in range(1, n+1):
        answer.append(i)
    result = permu(answer, k)
    return result

print(solution(3, 5))
