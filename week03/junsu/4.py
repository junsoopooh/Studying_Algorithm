def seperate(name):
    # head와 number를 분리하는 함수
    idx = 0
    head = ""
    number = ""

    # 처음 숫자가 나오기 전까지가 head
    while True:
        if name[idx] in "0123456789":
            head = name[:idx]
            break
        idx += 1

    # idx는 number의 첫글자로 유지된 상태에서 시작
    # 숫자가 나오면 계속 number로 추가
    # 5자리가 넘어가거나, tail이 존재하지 않으면 종료
    while len(number) < 5 and idx < len(name):
        if name[idx] in "0123456789":
            number += name[idx]
            idx += 1
        else:
            break
    # head는 소문자로 변환
    return head.lower(), number


def solution(files):
    # 정답을 담을 배열
    answer = []

    # 각기 다른 head만 담을 배열
    # 첫번째 정렬을 위해 사용
    head_order = []

    # 동일한 head를 가진 number들을 담을 배열
    # 두번째 정렬을 위해 사용
    # key는 head로, value는 list로 만들 것.
    # 원소는 [number, index] 형태로 만들어 number로 정렬한다.
    # index는 files 내에서 index를 뜻하며 원래 파일 이름을 찾을 수 있도록 한다.
    arr = dict()

    for i in range(len(files)):
        file = files[i]
        # 파일명에서 head, number 추출
        head, number = seperate(file)

        # 이번 파일의 head가 이전에 나온 적 있는 head라면?
        if arr.get(head):
            # dict에서 head가 key인 value를 찾아 추가
            arr[head].append([int(number), i])
        else:
            # 처음 나온 head라면 dict에 추가
            arr[head] = [[int(number), i]]
            # 새로운 head 이므로 head 배열에도 추가
            head_order.append(head)

    # head 배열을 사전순으로 정렬
    head_order.sort()

    # 가장 먼저 나와야할 head 선택
    for head in head_order:
        # 선택된 것을 head로 가지는 number 들을 정렬
        arr[head].sort()
        for num, idx in arr[head]:
            # 순서대로 원래 파일 이름을 정답 배열에 추가
            answer.append(files[idx])

    return answer
