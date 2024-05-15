# [조이스틱](https://school.programmers.co.kr/learn/courses/30/lessons/42860)

# 1차 55.6
def solution(name):
    def cal(x):
        max_val = ord("Z")+1
        return min(ord(name[x])-ord(tmp[x]),(max_val-ord(name[x])))
    n = len(name)
    name = list(name)
    answer = 0
    idx = 0
    tmp = list('A'*n)
    while True:
        print(tmp,idx,answer)
        if name[idx] != tmp[idx]:
            answer += cal(idx)
            tmp[idx] = name[idx]
        if name == tmp:
            break
        if cal((idx-1)%n) >= cal((idx+1)%n):
            idx = (idx-1)%n
        else:
            idx = (idx+1)%n
        answer += 1
    return answer


# 2차 51.9
def solution(name):
    def cal(x):
        max_val = ord("Z")+1
        return min(ord(name[x])-ord(tmp[x]),(max_val-ord(name[x])))
    n = len(name)
    name = list(name)
    answer = 0
    idx = 0
    tmp = list('A'*n)
    while True:
        if name[idx] != tmp[idx]:
            answer += cal(idx)
            tmp[idx] = name[idx]
        if name == tmp:
            break
        answer += 1
        for i in range(1,n):
            min_idx = idx-i
            max_idx = idx+i
            if cal(min_idx%n) > cal(max_idx%n):
                idx = (min_idx)%n
                break
            else:
                idx = (max_idx)%n
                break
    return answer

# 3차 7.4/100 https://velog.io/@kjy2134/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-%ED%8C%8C%EC%9D%B4%EC%8D%AC
def solution(name):
    n = len(name)
    name = list(name)
    tmp = list('A'*n)
    def cal(x):
        max_val = ord("Z")+1
        return min(ord(name[x])-ord('A'),(max_val-ord(name[x])))
    
    answer = 0
    cnt = 0
    for i in range(n):
        cnt += cal(i)
    

    for i in range(len(name)//2 + 1):
        left = name[-i:] + name[:-i] 
        right = name[i: :-1] + name[i+1:][::-1]
        for n in [left,right]:
            for x in range(len(left)-1,-1,-1):
                if n[x] != 'A':
                    break
            n = n[:x+1]

            answer = min(answer, answer + i)

    return answer+ cnt


# 4차 100/100
def solution(name):
    # 최솟값 구하기 위해 최댓값으로 설정
    answer = 10**9
    
    # 특정 글자를 만들기 위해 "A"에서 눌러야 할 조이스틱 조작 횟수를 반환하는 함수
    def cal(x):
        max_val = ord("Z")+1
        return min(ord(x)-ord('A'),(max_val-ord(x)))
    
    # 찍고 방향을 바꿀 지점을 절반까지로 설정. 절반을 넘어간 시점에서 뒤돌아 오는 것은 최솟값일리가 없음.
    for i in range(len(name)//2 + 1):
        # 시작지점에서 왼쪽으로 간 후 방향을 바꿔 오른쪽으로 계속 갔을 떄의 문자열
        left = name[-i:] + name[:-i] 
        # 시작지점에서 오른쪽으로 간 후 방향을 바꿔 왼쪽으로 계속 갔을 떄의 문자열
        right = name[i: :-1] + name[i+1:][::-1]
        # 두 경우를 모두 살펴봄
        for n in [left,right]:
            arr = []
            # 문자열을 살펴볼때 남은 것들이 모두 "A"라면 볼 필요가 없음
            # 뒤에서부터 어디까지가 "A"로만 이루어졌는지 확인하는 과정
            for x in range(len(left)-1,-1,-1):
                if n[x] != 'A':
                    break
            n = n[:x+1]
            # 각 글자들을 "A"에서 원하는대로 바꾸는데 까지 필요한 조작 수들을 배열에 담음
            for x in n:
                arr.append(cal(x))
            # i : 처음 커서를 움직인 방향으로 조작한 횟수
            # len(arr)-1 : 방향을 바꾼 후 커서를 움직이기 위한 조작 횟수
            # sum(arr) : 각 글자들을 원하는 글자로 바꾸기 위한 조작 횟수
            answer = min(answer, i + sum(arr)+len(arr)-1)

    return answer