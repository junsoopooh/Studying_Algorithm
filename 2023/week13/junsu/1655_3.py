import sys
from heapq import heappop, heappush, heappushpop

n = int(sys.stdin.readline())
large = [] # 가운뎃값보다 큰 배열
mid = [] # 가운뎃값 담는 배열 
small = [] # 가운덱값보다 작은 배열, 최소힙이기 때문에 음수로 바꿔서 넣고 뺄 예정
cnt = 0 # 초반 3개를 위한 설정
for _ in range(n):
    cnt += 1 # 입력한 숫자 체크
    num = int(sys.stdin.readline())
    if cnt == 1: # 처음 들어온 숫자는 무조건 출력
        heappush(mid,num) # 1개뿐일땐 가운데
        print(num)
    elif cnt == 2: # 두번째로 들어올때는 둘 중 작은 수
        tmp = heappushpop(mid,num) # 두 숫자 모두 mid에 들어있음
        print(tmp)
        heappush(large,heappop(mid)) # 두 숫자 중 큰 것은 large로 옮김
        heappush(mid,tmp) # 작은 것은 mid에 둔다.
    # 현재 mid에 한 개, large에 1개 들어있는 상태. 이제부턴 일반화 가능하므로 cnt는 신경안씀
    else:
        if len(large) == len(small): # 두 배열의 크기가 같다면 mid에는 1개뿐이므로 다음에 수가 들어오면 가운데값이 2개가 된다.
            if mid[0] > num: # 현재 가운뎃값보다 작은 값이 들어오면?
                num *= -1
                tmp = heappush(small,num) # 음수로 변환해 small에 넣은 후 pop하여 최대힙을 찾는다.
                tmp *= -1
                tmp = heappushpop(mid,tmp) # 찾은 최대힙을 mid에 넣고 최소힙을 찾는다.
                print(tmp) # 가운데 값중 작은 수를 출력해야하니 그대로 출력
                heappush(large,heappop(mid)) # mid에 남은 수는 큰 수 이므로 large로 넣는다.
                heappush(mid,tmp) # 아까 뺀 가운데 값을 다시 넣어준다.
                # 이 상황에서는 mid의 길이는 1이고 large의 길이가 small보다 1 더 길다.
            else: # 가운뎃값보다 큰 값이 들어왔다.
                tmp = heappush(large,num)  # large배열에 넣는다.
                tmp = heappop(mid) # 어차피 large배열에서 최소힙을 구해봤자 둘 중 더 작은 현재 mid의 원소를 출력해야하므로 굳이 꺼내지 않는다.
                print(tmp) # 가운뎃값 중 작은 수를 출력
                heappush(mid,tmp)
        else: # large와 small이 같지 않을 때는 항상 large가 더 크다. 가운데 값 둘 중 작은 수를 출력하고 큰 수는 large에 넣도록 로직이 되있으므로.
            if mid[0] > num: # 현재 가운뎃값보다 더 작은 수가 들어옴
                num *= -1 # 음수로 변환
                heappush(small,num) # 가운뎃값은 하나므로 배열의 길이가 1 작은 small 에 넣고 현재 가운뎃값 그대로 다시 출력하면된다.
                tmp = heappop(mid)
                print(tmp)
                heappush(mid,tmp)
            else: # 현재 가운뎃값보다 더 큰 수가 들어옴
                tmp = heappop(mid) # 현재 가운뎃값은 음수로 변환해 small배열에 넣는다.
                tmp *= -1
                heappush(small,tmp)
                tmp = heappushpop(large,num) # 새로 들어온 수를 large 배열에 넣고 최소힙을 구한다.
                heappush(mid,tmp) # 구한 최소 heap을 새로운 가운뎃값으로 설정
                print(tmp)