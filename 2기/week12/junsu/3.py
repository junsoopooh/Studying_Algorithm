# N개의 최소공배수
def solution(arr):
    num = max(arr)
    i = 1
    while True:
        answer = num*i
        for x in arr:
            if answer%x:
                i += 1
                break
        else:
            return answer
    
