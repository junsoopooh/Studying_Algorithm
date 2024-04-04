# [N진수 게임](https://school.programmers.co.kr/learn/courses/30/lessons/17687)

# 1차시도 실패
# 진법을 바꿔 변환하는 함수 만들려고 했으나 실패..
def find_limit(a,b):
    # a를 b진법으로 바꿀 때 자릿수를 반환
    idx = 0
    while b**idx < a:
        idx += 1
    return idx

def change(k,m):
    # k를 m진법으로 변환하는 함수
    max_val = find_limit(k,m)
    arr = [0 for _ in range(max_val)]
    for i in range(max_val):
        arr[i] = k//(m**(max_val-(i+1)))
        k -= arr[i]*(m**(max_val-(i+1)))
    return str(''.join(arr))

def solution(n, t, m, p):
    answer = ''
    arr = []
    numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    n_numbers = numbers[:n]
    for i in range(m*t):
        num = change(i,n)
        print(num)
    return answer


# 2차시도
# 변환하는 함수 보고 만듬.
# 모두 나열한 댜음 각 차례때의 문자를 더함
def change(n, base):
    numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    q, r = divmod(n, base)

    if q == 0:
        return numbers[r]
    else:
        return change(q, base) + numbers[r]

def solution(n, t, m, p):
    answer = ''
    arr = []
    for i in range(m*t):
        arr += list(change(i,n))
    
    for j in range(t):
        answer += arr[t]
    return answer


# 3차시도
# 인덱스와 순서의 차이(0)을 고려하기위해 'x'를 추가
def change(n, base):
    numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    q, r = divmod(n, base)

    if q == 0:
        return numbers[r]
    else:
        return change(q, base) + numbers[r]

def solution(n, t, m, p):
    answer = ''
    arr = ['x']
    for i in range(m*t):
        arr += list(change(i,n))
    
    for j in range(t):
        answer += arr[p+j*m]
    return answer