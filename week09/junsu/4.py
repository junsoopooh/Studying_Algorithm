# 행렬의 곱셈
def solution(arr1, arr2):
    a1 = len(arr1)
    b1 = len(arr1[0])
    a2 = len(arr2)
    b2 = len(arr2[0])
    answer = [[0 for _ in range(b2)] for _ in range(a1)]
    for i in range(a1):
        for j in range(b2):
            tmp = 0
            for x in range(b1):
                tmp += (arr1[i][x]*arr2[x][j])
            answer[i][j] = tmp
    return answer
