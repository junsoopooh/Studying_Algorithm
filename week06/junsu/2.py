# [다트 게임](https://school.programmers.co.kr/learn/courses/30/lessons/17682)

def solution(dartResult):
    idx = 0
    scores = []
    
    # while문 1회 마다 1차례의 결과를 체크
    while idx < len(dartResult):
        # 점수 부분을 담을 변수
        tmp = 0
        # 문자열이 숫자 부분이라면 점수를 의미
        if dartResult[idx].isdigit():
            # 그 다음 문자도 숫자라면 10이라는 의미이므로 2글자 모두 담는다.
            if dartResult[idx+1].isdigit():
                tmp = int(dartResult[idx]+dartResult[idx+1])
                # 다다음 글자를 보기위해 index 증가
                idx += 2
            # 아니면 1자리 숫자이므로 1글자만 담는다.
            else:
                tmp = int(dartResult[idx])
                # 다음 글자를 보기위해 index 증가
                idx += 1
        
        # 알파벳이 나오면 보너스를 의미
        if dartResult[idx].isalpha():
            if dartResult[idx] == 'D':
                tmp = tmp**2
            elif dartResult[idx] == 'T':
                tmp = tmp**3
            # 다음 글자를 살피기 위해 idx 증가
            idx += 1
        scores.append(tmp)
        
        # 옵션은 없을수도 있음
        # 마지막 차례에 옵션이 없어서 더이상 글자가 없을 경우를 고려하여 예외처리가 필요
        if idx >= len(dartResult):
            break
        
        # 옵션이 있다면
        if dartResult[idx] in ['*','#']:
            # 스타상의 경우 가장 최근 점수의 2배 증가
            if dartResult[idx] == '*':
                scores[-1] = 2*scores[-1]
                # 첫번째 다트 기회에 스타상이 나올 경우에는 그 이전 점수는 증가시키지 않음
                # 따라서 그 이전 점수가 존재할때만 그것도 2배 증가
                if len(scores) > 1:
                    scores[-2] = 2*scores[-2]
            # 아차상은 그 전점수의 부호를 변경
            else:
                if scores:
                    scores[-1] = -1*scores[-1]
            idx += 1
               
    return sum(scores)