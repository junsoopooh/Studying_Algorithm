# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    def translate(p):
        if p >=2:
            return 7-p
        else:
            return 6
    
    answer = []
    cnt = 0
    unknown = 0
    for num in lottos:
        if not num:
            unknown += 1
            continue
        if num in win_nums:
            cnt += 1
            continue
    max_match = cnt + unknown
    min_match = cnt
    answer.append(translate(max_match))
    answer.append(translate(min_match))
    return answer
