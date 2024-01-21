#키패드 누르기
def solution(numbers, hand):
    arr = [0 for _ in range(len(numbers))]
    position = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],False,[3,2]]
    finger = [10,12]
    left = [1,4,7]
    right = [3,6,9]
    for i in range(len(numbers)):
        num = numbers[i]
        if num in left:
            arr[i] = 'L'
            finger[0] = num
        elif num in right:
            arr[i] = 'R'
            finger[1] = num
        else:
            number_position = position[num]
            left_finger = position[finger[0]]
            right_finger = position[finger[1]]
            distance_left = abs(number_position[0]-left_finger[0]) + abs(number_position[1]-left_finger[1])
            distance_right = abs(number_position[0]-right_finger[0]) + abs(number_position[1]-right_finger[1])
            if distance_left < distance_right:
                arr[i] = 'L'
                finger[0] = num
            elif distance_left > distance_right:
                arr[i] = 'R'
                finger[1] = num
            else:
                if hand == 'left':
                    arr[i] = 'L'
                    finger[0] = num
                else:
                    arr[i] = 'R'
                    finger[1] = num
    answer = "".join(arr)
    return answer
