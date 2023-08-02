# 각 자리수의 합으로 나누어 떨어지면 하샤드 수

x = 13

def solution(x):
    all_sum = sum(int(e) for e in str(x))
    answer = True if x % all_sum == 0 else False
    return answer

print(solution(x))