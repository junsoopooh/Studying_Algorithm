from collections import deque
import math

def solution(str1,str2):
    a = []
    b = []

    # 다중집합 만들기(특수문자,공백등 제외) - str1
    for i in range(1, len(str1)):
        tmp = str1[i - 1] + str1[i]
        for i in tmp:
            if (ord(i) >= 32 and ord(i) <= 64) or (ord(i) >= 91 and ord(i) <= 96) or ord(i) >= 123:
                break
        else:
            a.append(tmp.lower())
    # 다중집합 만들기(특수문자,공백등 제외) - str2
    for i in range(1, len(str2)):
        tmp = str2[i - 1] + str2[i]
        for i in tmp:
            if (ord(i) >= 32 and ord(i) <= 64) or (ord(i) >= 91 and ord(i) <= 96) or ord(i) >= 123:
                break
        else:
            b.append(tmp.lower())

    a.sort()
    b.sort()

    a = deque(a)
    b = deque(b)

    # 교집합
    inner = []
    # 합집합
    plus = []

    # 길이가 더 긴 리스트 기준
    if len(a) >= len(b):
        while a:
            # 처음 값 pop
            valA = a.popleft()
            for i in range(len(b)):
                # 처음 값을
                if b[i] == valA:
                    inner.append(valA)
                    b.remove(b[i])
                    break
            else:
                plus.append(valA)

        for i in inner:
            plus.append(i)
        while b:
            plus.append(b.popleft())
    else:
        while b:
            valB = b.popleft()
            for i in range(len(a)):
                if a[i] == valB:
                    inner.append(valB)
                    a.remove(a[i])
                    break
            else:
                plus.append(valB)

        for i in inner:
            plus.append(i)
        while a:
            plus.append(a.popleft())

    if len(inner) == 0 and len(plus) == 0:
        return 65536

    Jak = len(inner) / len(plus)

    answer = math.trunc(Jak * 65536)


from collections import deque
import copy

st = "qwertyuiopasdfghjklzxcvbnm"


def solution(str1, str2):
    # 소문자로 변경
    str1 = str1.lower()
    str2 = str2.lower()

    news_str1 = []
    news_str2 = []

    # 입력 예외 형식 조건을 제외한 집합1
    for i in range(1, len(str1)):
        if str1[i] in st and str1[i - 1] in st:
            tmp = []
            tmp.append(str1[i - 1])
            tmp.append(str1[i])
            news_str1.append("".join(tmp))
    # 입력 예외 형식 조건을 제외한 집합2
    for i in range(1, len(str2)):
        if str2[i] in st and str2[i - 1] in st:
            tmp = []
            tmp.append(str2[i - 1])
            tmp.append(str2[i])
            news_str2.append("".join(tmp))

    # 집합1과 집합2가 모두 공집합인경우
    if len(news_str1) == 0 and len(news_str2) == 0:
        return 65536

    # 길이 기준으로 deque로 초기화
    if len(news_str1) >= len(news_str2):
        newsA = deque(news_str2)
        newsB = deque(news_str1)
    else:
        newsA = deque(news_str1)
        newsB = deque(news_str2)

    newA = deque()
    innerSet = []

    # 교집합 구하기
    while newsA:
        target = newsA.popleft()
        for b in range(len(newsB)):
            if b == target:
                innerSet.append(target)
            else:
                newA.append(target)
            delIdx = b
        del newsB[b]

    # 합집합을 구하기위한 복사본들
    innerSet_A = deque(copy.deepcopy(innerSet))
    innerSet_B = deque(copy.deepcopy(innerSet))

    # 합집합 구하기
    # B - A

    while innerSet_B:
        target = innerSet_B.popleft()
        for i in range(len(newsB)):
            if newsB[i] == target:
                delIdx = i
                break
        del newsB[i]

    print('B - A', newsB)
    print('inner : ', innerSet)

    # A - B
    # if len(newsA) > 1:
    #     while innerSet_A:
    #         target = innerSet_A.popleft()
    #         for i in range(len(newA)):
    #             if newsA[i] == target:
    #                 delIdx = i
    #                 break
    #         del newsA[i]

    print('A - B :', newA)

    plusResult = len(newsA) + len(innerSet) + len(newsB)
    innerResult = len(innerSet)
    print(plusResult, innerResult)
    answer = (innerResult / plusResult)

    return answer