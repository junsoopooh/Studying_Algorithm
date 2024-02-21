def solution(arr):
    answer = 0
    arr = sorted(arr)
    maxVal = arr[-1]
    arr = arr[:-1]
    idx = 1
    targetVal = 0
    while 1:
        cnt = 0
        targetVal = maxVal * idx
        for i in range(len(arr)):
            if targetVal % arr[i] == 0:
                cnt += 1

        if cnt == len(arr):
            print(targetVal)
            answer = targetVal
            break
        idx += 1

    return answer