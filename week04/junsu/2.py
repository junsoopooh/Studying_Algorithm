# 체육복 https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 93.3/100
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    arr = set()

    for loser in lost:
        if loser in reserve:
            reserve.remove(loser)
            continue

        if loser - 1 in reserve:
            reserve.remove(loser - 1)
        elif loser + 1 in reserve:
            reserve.remove(loser + 1)
        else:
            arr.add(loser)
    return n - len(arr)


# 2차 100/100
def solution(n, lost, reserve):
    # 항상 빌려주는 방향이 일정해야함
    # 예를 들어, 2,4번 학생이 도둑맞고 1,3번 학생이 여벌이 있는 경우
    # 1번 학생이 2번 학생에게 빌려주고 3번 학생이 4번 학생에게 빌려주는 것이 최선
    # 만약 3번 학생이 2번 학생에게 빌려주게 되면 4번 학생은 빌려받을 수 없음
    # 이를 방지하기 위해, 번호가 낮은 학생부터 자신보다 더 낮은 번호의 학생에게 빌리는 것을 우선으로 함
    # 이후 자신보다 1 큰 번호의 학생에게 빌릴 수 있는지 확인
    lost.sort()
    reserve.sort()

    arr = set()
    real_lost = []

    # 여벌이 있었으나 도둑맞은 사람은 빌릴 필요도 없고 빌려줄 수도 없으므로 제외
    for loser in lost:
        if loser in reserve:
            reserve.remove(loser)
        else:
            real_lost.append(loser)

    # 정말 빌릴 필요가 있는 학생들의 배열을 탐색
    for loser in real_lost:
        # 한 치수 작은 학생이 빌려줄 수 있는지 먼저 탐색
        if loser - 1 in reserve:
            reserve.remove(loser - 1)

        # 한 치수 큰 학생이 빌려줄 수 있는지 먼저 탐색
        elif loser + 1 in reserve:
            reserve.remove(loser + 1)

        # 누구에게도 빌릴 수 없다면 배열에 추가
        else:
            arr.add(loser)
    return n - len(arr)
