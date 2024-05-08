# [괄호 변환](https://school.programmers.co.kr/learn/courses/30/lessons/60058)

from collections import Counter

# 균형잡힌 괄후 문자열인지 확인하는 함수
def check_balance(k):
    arr = Counter(k)
    if arr['('] == arr[')']:
        return True
    return False

# 올바른 괄호 문자열인지 확인하는 함수
def check_right(k):
    while '()' in k:
        arr = list(k)
        for i in range(len(k)-1):
            if arr[i] == '(' and arr[i+1] == ')':
                arr[i] = arr[i+1] = ''
        k = ''.join(arr)
    if not len(k):
        return True
    return False

# 변환과정을 나타내는 함수
def process(x):
    # 1단계
    if not x:
        return x
    
    # 2단계
    for i in range(1,len(x)+1):
        tmp = x[:i]
        if check_balance(tmp):
            break
    u = tmp
    v = x[i:]
    
    # 3단계
    if check_right(u):
        # 3-1단계
        return u + process(v)
    # 4단계
    else:
        # 4-1, 4-2, 4-3단계
        new = '(' + process(v) + ')'
        arr = []
        # 4-4단계
        for i in range(1,len(u)-1):
            if u[i] == '(':
                arr.append(')')
            else:
                arr.append('(')
        new += ''.join(arr)
        # 4-5단계
        return new

def solution(p):
    answer = ''
    u = ''
    answer = process(p)
    return answer