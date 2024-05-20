# [모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840)

# 수포자 1이 찍은 답을 문제 번호로 찾기
def first_answer(idx):
    if (idx+1) % 5:
        return (idx+1) % 5
    else:
        return 5

# 수포자 2가 찍은 답을 문제 번호로 찾기


def second_answer(idx):
    if not idx % 2:
        return 2
    else:
        if idx % 8 == 1:
            return 1
        elif idx % 8 == 3:
            return 3
        elif idx % 8 == 5:
            return 4
        else:
            return 5

# 수포자 3이 찍은 답을 문제 번호로 찾기


def third_answer(idx):
    idx %= 10
    if idx < 2:
        return 3
    elif idx < 4:
        return 1
    elif idx < 6:
        return 2
    elif idx < 8:
        return 4
    else:
        return 5


def solution(answers):
    ans = []
    # 맞춘 갯수를 담는 배열
    arr = [0, 0, 0]
    # 채점
    for idx in range(len(answers)):
        if answers[idx] == first_answer(idx):
            arr[0] += 1
        if answers[idx] == second_answer(idx):
            arr[1] += 1
        if answers[idx] == third_answer(idx):
            arr[2] += 1

    # 가장 많이 맞춘 사람 찾기
    max_val = max(arr)
    # 고득점자가 한 명일 경우
    if len(set(arr)) == 3:
        ans.append(arr.index(max_val)+1)
    # 고득점자가 둘 이상일 경우
    else:
        for i in range(3):
            if arr[i] == max_val:
                ans.append(i+1)
    return ans
