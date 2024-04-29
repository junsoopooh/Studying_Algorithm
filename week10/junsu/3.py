def solution(progresses, speeds):
    answer = []
    idx = 0
    while idx < len(progresses):
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while idx < len(progresses):
            if progresses[idx] >= 100:
                idx += 1
                cnt += 1
            else:
                break
        if cnt:
            answer.append(cnt)
    return answer