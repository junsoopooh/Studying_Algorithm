# 햄버거 만들기
# 1번째 시도(오답)
def solution(ingredient):
    answer = 0
    arr = [1,2,3,1]
    while True:
        idx = 0
        for x in range(len(ingredient)):
            if idx ==4:
                answer += 1
                break
            if ingredient[x] == arr[idx]:
                idx += 1
                ingredient[x] = 10
        else:
            if idx == 4:
                answer += 1
            else:
                return answer

# 2번째 시도(정답)
def solution(ingredient):
    answer = 0
    tmp = []
    burger = [1,2,3,1]
    
    for x in ingredient:
        tmp.append(x)
        if tmp[-4:] == burger:
            answer += 1
            for _ in range(4):
                tmp.pop()
    return answer