# 그리디
def solution(n, m, section):
    section.sort()
    
    answer = 0
    i = 0
    while i < len(section): # 섹션 안의 값들만 다 칠해지면 됨

        # 롤러의 커버 범위
        start = section[i]
        end = start + m - 1
        
        while i < len(section) and section[i] <= end: # 롤러가 커버하는 만큼 섹션을 건너뜀
            i += 1
        
        answer += 1
    
    return answer
        
        