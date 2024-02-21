from collections import defaultdict

'''
 1. survey를 돌며 하나씩 확인
 1-1. 각 survey의 앞(부정) 뒤(부정)
 2. 각 인덱스의 choices랑 비교하여 점수 선택
 2-1. 선택한 점수에 따라 answer에 알맞은 string join

---> 문제 이해 잘못함 regame

 0. dictionary 초기화
 1. survey를 돌며 하나씩 확인
 1-1. 각 survey의 앞(부정) 뒤(부정)
 2. 각 인덱스의 choices랑 비교하여 점수 선택 하여 알맞은 Dic ++
 3. dic 4번 반복문을 통해 알맞은 답 찾기

'''


def solution(survey, choices):
    surveyDic = defaultdict(int)
    answer = ''

    for s in range(len(survey)):
        NotAgree = survey[s][0]
        Agree = survey[s][1]
        choiceScore = choices[s]
        if choiceScore >= 5:
            surveyDic[Agree] += choiceScore - 4
        elif choiceScore <= 3:
            surveyDic[NotAgree] += 4 - choiceScore
        else:
            surveyDic[Agree] += 1
            surveyDic[NotAgree] += 1

    for i in range(4):
        if i == 0:
            if surveyDic['R'] > surveyDic['T']:
                answer += 'R'
            elif surveyDic['R'] < surveyDic['T']:
                answer += 'T'
            else:
                answer += 'R'
        elif i == 1:
            if surveyDic['C'] > surveyDic['F']:
                answer += 'C'
            elif surveyDic['C'] < surveyDic['F']:
                answer += 'F'
            else:
                answer += 'C'
        elif i == 2:
            if surveyDic['J'] > surveyDic['M']:
                answer += 'J'
            elif surveyDic['J'] < surveyDic['M']:
                answer += 'M'
            else:
                answer += 'J'
        else:
            if surveyDic['A'] > surveyDic['N']:
                answer += 'A'
            elif surveyDic['A'] < surveyDic['N']:
                answer += 'N'
            else:
                answer += 'A'

    return answer

