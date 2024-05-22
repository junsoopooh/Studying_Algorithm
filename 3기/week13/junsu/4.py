# [오픈채팅방](https://school.programmers.co.kr/learn/courses/30/lessons/42888)

def solution(record):
    n = len(record)
    answer = []
    # 들어오거나 나가는 행동을 저장할 배열
    arr = dict()
    # 각 아이디의 최종 닉네임을 저장하기 위한 배열
    name = dict()
    # 데이터를 가공하기 위한 반복문
    for i in range(n):
        # 데이터 분리
        data = list(record[i].split(" "))
        tmp = dict()
        # 들어오고 나가는 행동이면 저장
        if data[0] != "Change":
            tmp["message"] = data[0]
            tmp["id"] = data[1]
            arr[i] = tmp
            # 들어올 때 닉네임을 바꾸는 경우 추적
            if data[0] == 'Enter':
                name[data[1]] = data[2]
        # 닉네임을 바꾸는 행동일땐 저장하지 않고 이름만 갱신
        else:
            name[data[1]] = data[2]

    # 출력하기 위한 반복문
    for i in range(n):
        # i번째일때 바꾸는 행동이였으면 arr에 해당 키 값은 존재하지 않음
        if i not in arr:
            continue

        # 각 아이디의 최종 닉네임으로 출력
        if arr[i]["message"] == "Enter":
            c = name[arr[i]["id"]] + "님이 들어왔습니다."
        elif arr[i]["message"] == "Leave":
            c = name[arr[i]["id"]] + "님이 나갔습니다."
        answer.append(c)
    return answer
