#JadenCase 문자열 만들기
def solution(s):
    arr = [' '] + list(s)
    nums = ['1','2','3','4','5','6','7','8','9','0',' ']
    n = len(arr)
    for i in range(1,n):
        if arr[i-1] == ' ' and arr[i] not in nums:
            arr[i] = arr[i].upper()
        elif arr[i].isupper():
            arr[i] = arr[i].lower()
    answer = ''.join(arr[1:])
    return answer
