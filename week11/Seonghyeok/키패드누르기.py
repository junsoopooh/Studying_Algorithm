def coordinate(num):
    handPhone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    for i in range(4):
        for j in range(3):
            if num == handPhone[i][j]:
                return [i + 1, j + 1]


def solution(numbers, hand):
    answer = ''

    LeftLocation = [4, 1]
    RightLocation = [4, 3]

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            if num == 1:
                LeftLocation = [1, 1]
            elif num == 4:
                LeftLocation = [2, 1]
            else:
                LeftLocation = [3, 1]
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            if num == 3:
                RightLocation = [1, 3]
            elif num == 6:
                RightLocation = [2, 3]
            else:
                RightLocation = [3, 3]
        else:
            target = coordinate(num)
            L = abs(LeftLocation[0] - target[0]) + abs(LeftLocation[1] - target[1])
            R = abs(RightLocation[0] - target[0]) + abs(RightLocation[1] - target[1])

            # R이 더 작을때
            if L > R:
                answer += 'R'
                if num == 2:
                    RightLocation = [1, 2]
                elif num == 5:
                    RightLocation = [2, 2]
                elif num == 8:
                    RightLocation = [3, 2]
                elif num == 0:
                    RightLocation = [4, 2]
            # L이 더 작을때
            elif R > L:
                answer += 'L'
                if num == 2:
                    LeftLocation = [1, 2]
                elif num == 5:
                    LeftLocation = [2, 2]
                elif num == 8:
                    LeftLocation = [3, 2]
                elif num == 0:
                    LeftLocation = [4, 2]
            else:
                if hand == "right":
                    answer += 'R'
                    if num == 2:
                        RightLocation = [1, 2]
                    elif num == 5:
                        RightLocation = [2, 2]
                    elif num == 8:
                        RightLocation = [3, 2]
                    elif num == 0:
                        RightLocation = [4, 2]
                elif hand == "left":
                    answer += 'L'
                    if num == 2:
                        LeftLocation = [1, 2]
                    elif num == 5:
                        LeftLocation = [2, 2]
                    elif num == 8:
                        LeftLocation = [3, 2]
                    elif num == 0:
                        LeftLocation = [4, 2]

    return answer