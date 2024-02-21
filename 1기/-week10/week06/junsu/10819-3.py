import sys #순열 안쓰려는 고집의 결과

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
idx = [] # 값을 담지 말고 index를 담을 계획이다.
visited = [False]*n
max_val = -10**6 # 그냥 적당히 작은 값넣었음. 최댓값 구할거니까


def dfs(x): # x는 dfs 깊이
    global max_val # 리스트에 넣어 최댓값을 구하기엔 8! = 40320이라 비효율적이라 판단했음
    if x == n: # n개 모두 정렬 했다면
        tmp = 0 # 더한 값 저장 변수 초기화
        for i in range(n-1): # i행과 그 다음행이므로 n-1까지 해야 index 범위 안벗어남
            tmp += abs(nums[idx[i]] - nums[idx[i+1]]) # 값이 아닌 index를 저장했으므로 idx[i]를 넣어준다.
        max_val = max(max_val, tmp) # 다 더한 값과 현재까지 최댓값 비교하여 업데이트
        return # 함수종료
    for i in range(n):
        if not visited[i]: # 아직 정렬하지 않은 원소라면
            visited[i] = True # 방문처리
            idx.append(i) # 그 원소의 index를 새로운 배열에 저장
            x += 1 # 깊이 1 증가
            dfs(x) # dfs
            x -= 1 # 초기화 과정
            idx.pop()
            visited[i] = False


dfs(0)
print(max_val)
