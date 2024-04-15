# [실패율](https://programmers.co.kr/learn/courses/30/lessons/42889)

# 1차시도: 100/100 수행속도가 느리다.
def solution(N, stages):
    answer = []
    arr = [0 for _ in range(N+2)]
    arr_f = [0 for _ in range(N+2)]
    for i in range(len(stages)):
        now = stages[i]
        for j in range(1,now+1):
            arr[j] += 1
        arr_f[now] += 1
    tmp = []
    for i in range(1,N+1):
        if arr[i] == 0:
            tmp.append([0,i])
        else:
            tmp.append([(arr_f[i]/arr[i]),i])
    tmp.sort(reverse=True, key=lambda x : (x[0],-x[1]))
    for i in range(N):
        answer.append(tmp[i][1])
    return answer