import sys
input = sys.stdin.readline

# n개의 점
n = int(input())

# 점들 좌표 x, y
dots = [list(map(int, input().split())) for _ in range(n)]
dots.sort()

# 두 점 사이의 거리
def distance (a1, a2):
    return (a1[0] - a2[0]) ** 2 + (a1[1] - a2[1]) ** 2

def search (left, right):
    # 시간초과: 다 훑지 않고 찾아보려면?
    # 1) 일단 x축을 기준으로 이분탐색 -> 최소값의 좌표값을 리스트에 추가
    # 2) 해당 리스트를 바탕으로 y축 기준 탐색

    # !!! 같을 경우도 고려 !!!
    if left == right:
        return sys.maxsize
    
    if right - left == 1:
        return distance(dots[left], dots[right])
    
    mid = (left + right) // 2
    mindistance = min(search(left, mid), search(mid, right))

    # x축 기준으로 탐색
    xlist = []
    for i in range(left, right+1):
        # !!! mid와 비교하는 것 !!!
        if (dots[mid][0] - dots[i][0]) ** 2 < mindistance:
            xlist.append(dots[i])

    xlist.sort(key= lambda x: x[1])
    length = len(xlist)

    # y축 기준으로 탐색
    for i in range(length-1):
        for j in range(i+1, length):
            if (dots[i][1] - dots[j][1]) ** 2 < mindistance:
                # y축 기준으로 mindistance보다 작다면,
                # 거리 계산해보기
                mindistance = min(distance(dots[i], dots[j]), mindistance)

    return mindistance

# left, right의 인덱스           
print(search(0, n-1))

# [시간 초과]
# # 일단 다 훑어보면서 확인해보자
# def search ():
#     # 두 점 거리의 제곱 리턴
#     result = []

#     for i in range(n-1):
#         for j in range(i+1, n):
#             distance1 = (dots[i][0] - dots[j][0]) ** 2
#             distance2 = (dots[i][1] - dots[j][1]) ** 2
#             result.append(distance1 + distance2)

#     return min(result)

# print(search())