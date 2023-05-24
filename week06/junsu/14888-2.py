import sys

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
plus,minus,multiple,division = map(int,sys.stdin.readline().split())
# 이전에는 더하기, 빼기, 곱하기, 나누기 모두 함수를 정의했었는데 굳이 그럴 필요는 없을것 같았다.
arr = [] 
def dfs(tmp,cnt,a,b,c,d): #tmp : 현재까지 계산 값, cnt : 연산 횟수 , a b c d : 덧셈, 뺄셈, 곱셈, 나눗셈 남은 횟수
    if cnt == n: # 연산 모두 마치면
        arr.append(tmp) # 리스트에 현재 값 삽입
        return # 함수 종료
    
    if a: # 더하기 연산 횟수가 남았다면
        tmp += nums[cnt] # 덧셈
        a -= 1 # 더하기 연산 횟수 1 감소
        cnt += 1 # 연산 횟수 1 증가
        dfs(tmp,cnt,a,b,c,d) # dfs
        cnt -= 1 # 다시 초기화 과정
        a += 1
        tmp -= nums[cnt]
    
    if b: # 뺄셈
        tmp -= nums[cnt]
        b -= 1
        cnt += 1
        dfs(tmp,cnt,a,b,c,d)
        cnt -= 1
        b += 1
        tmp += nums[cnt]

    if c: #곱셈
        tmp *= nums[cnt]
        c -= 1
        cnt += 1
        dfs(tmp,cnt,a,b,c,d)
        cnt -= 1
        c += 1
        tmp = tmp // nums[cnt]

    if d: # 나눗셈, nums의 수는 문제 조건에 따라 항상 양수이다. tmp의 부호를 기준으로 나누면 된다. 아마 0으로 나누는 경우를
        if tmp >= 0: # 배제하기 위함인듯 하다.
            tmp = tmp//nums[cnt] # 양수면 그대로 나눠서 몫만 취한다
        else:
            r_tmp = abs(tmp)//nums[cnt] # tmp가 음수면 절댓값을 이용해 양수로 바꾼후 연산한다.
            tmp = -1 * r_tmp # 값을 저장한후 -1 을 곱해 부호 바꾸는 과정이 나누어지지 않으면 오답 발생한다.
        d -= 1 # 기존에 tmp = (-1)*abs(tmp)//nums[cnt] 로 해서 오답이였는데 음수 나눗셈을 그대로 실행해버려 나온 결과인듯
        cnt += 1
        dfs(tmp,cnt,a,b,c,d)
        cnt -= 1
        d += 1
        if tmp >= 0: # 위와 동일하다.
            tmp = abs(tmp)*nums[cnt]
        else:
            r_tmp = abs(tmp)*nums[cnt]
            tmp = -1* r_tmp
        
dfs(nums[0],1,plus,minus,multiple,division) # 맨 처음값은 맨 처음 입력받은 숫자, 숫자 하나 들어갔으니 연산 1회
print(max(arr))
print(min(arr))
