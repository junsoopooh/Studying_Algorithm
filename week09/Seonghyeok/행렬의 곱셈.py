def solution(arr1, arr2):
    answer = []
    column = []

    # arr2 열 기준으로 다시 정렬
    for i in range(len(arr2[0])):
        tmp = []
        for j in range(len(arr2)):
            tmp.append(arr2[j][i])
        column.append(tmp)

    for i in range(len(arr1)):
        tmp = []
        for j in range(len(column)):
            val = 0
            for k in range(len(column[0])):
                val += (arr1[i][k] * column[j][k])
            tmp.append(val)
        answer.append(tmp)

    return answer
