# [옹알이 (2)](https://school.programmers.co.kr/learn/courses/30/lessons/133499)
def search_index(arr,k):
    result = -1
    if k in arr:
        result = arr.index(k)
    return result

def solution(babbling):
    answer = 0
    arr = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        idx = 0
        n = len(word)
        last_find_idx = -1
        while idx <= n:
            if not n:
                answer += 1
                break
            tmp = word[:idx+1]
            search_result = search_index(arr,tmp)
            if search_result != -1 and search_result != last_find_idx:
                last_find_idx = search_index(arr,tmp)
                word = word[idx+1:]
                n = len(word)
                idx = 0
            else:
                idx += 1
                
    return answer