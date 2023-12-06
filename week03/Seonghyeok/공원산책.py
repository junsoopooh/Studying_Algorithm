def solution(park, routes):
    '''
    흠 ... 무조건 행렬이 특정한 크기가 아닐수도있는건가
    예외를 생각해보쟈
    '''
    parkList = []
    target_index = 0
    # 공원을 나타내는 2차원 배열 초기화
    for i in park:
        parkList.append(list(i))

    # start index 찾기 
    for i in range(len(parkList)):
        for j, target in enumerate(parkList[i]):
            if target == 'S':
                target_index = [i, j]
                break
    print(target_index)
    # 행
    column = len(parkList[0])
    # 열
    row =  len(parkList)
    print('column : ',column ,'row : ', row)

    for val in routes:
        op = val[0]
        num = int(val[2])

        if op == 'E':
            for i in range(1,num+1):
                target_index[1] += 1
                if target_index[1] >= column:
                    target_index[1] -= i
                    break
                elif parkList[target_index[0]][target_index[1]] == 'X':
                    target_index[1] -= i
                    break
        elif op == 'W':
            for i in range(1, num+1):
                target_index[1] -= 1
                if target_index[1] < 0:
                    target_index[1] += i
                    break
                elif parkList[target_index[0]][target_index[1]] == 'X':
                    target_index[1] += i
                    break
        elif op == 'S':
            for i in range(1, num+1):
                target_index[0] += 1
                if target_index[0] >= row:
                    target_index[0] -= i
                    break
                elif parkList[target_index[0]][target_index[1]] == 'X':
                    target_index[0] -= i
                    break
        elif op == 'N':
            for i in range(1, num+1):
                target_index[0] -= 1
                if target_index[0] < 0:
                    target_index[0] += i
                    break
                elif parkList[target_index[0]][target_index[1]] == 'X':
                    target_index[0] += i
                    break
    return target_index

# 위 확인
# print(solution(["OSO", "XOX", "OXO"], ["N 1", "N 1"]))
# 아래 확인
#print(solution(["OSO", "XOO", "OOO"], ["S 2","S 1","E 1", "S 1"]))
# 왼쪽 확인
print(solution(["OXO", "OSO", "OXO"], ["W 2", "W 1", "S 1"]))
# # 오른쪽 확인
# print(solution(["OXO", "XSX", "OXO"], ["S 1", "E 1", "W 1", "N 1"]))

#    0 1
# 0 [0 0]
# 1 [0 0]
# -> 동쪽 끝 2이상 X
# -> 남쪽 끝 2이상 X
# -> 북쪽 끝 0미만 X
# -> 서쪽 끝 0 미만 X
