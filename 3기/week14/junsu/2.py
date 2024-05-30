# [후보키](https://school.programmers.co.kr/learn/courses/30/lessons/42890)
from itertools import combinations

# 최소성을 만족하는지 확인하는 함수
# 검증하는 조합 target의 부분집합이 이미 찾은 조합 answer_array에 포함되어 있는지 확인
# 포함되어 있으면 target은 최소성을 만족하지 않음
def validate(answer_array,target):
    for i in answer_array:
        if set(i).issubset(target):
            return False
    return True

def solution(relation):
    answer = []
    n = len(relation)
    m = len(relation[0])
    arr = [ i for i in range(m)]
    
    for i in range(m):
        # 모든 속성 조합을 구함.
        idx = list(combinations(arr,i+1))
        for q in idx:
            # 유일성을 만족하는지 확인
            # 속성의 값을 이은 문자열을 set에 넣어 중복을 제거
            # 중복이 없다면 유일성을 만족
            check = set()
            for j in range(n):
                tmp = ""
                for k in q:
                    tmp += relation[j][k]
                check.add(tmp)
            # set의 길이가 n과 같다면 중복이 없단 의미로 유일성을 만족
            if len(check) == n:
                # 최소성을 만족하는지 확인
                if validate(answer,q):
                    answer.append(q)
    return len(answer)