# 문자열 나누기
def solution(s):
    answer = 0
    while s:
        x = s[0]
        num_x = 0
        not_x = 0
        for i in range(len(s)):
            if s[i] == x:
                num_x += 1
            else:
                not_x += 1
            if num_x == not_x:
                answer += 1
                s = s[i+1:]
                break
        else:
            return answer+1
    return answer
        
