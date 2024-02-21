import sys

n = int(sys.stdin.readline())
stars = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    stars.append([a,b])

# 풀이 과정에 대한 개략적 설명
# 어떤 영역 내에서 두점 사이의 거리가 가장 작은것을 구하려고 함. 따라서 영역을 반으로 나누어, 각각에서 가장 작은 두점 사이의 거리를 구한다. 각 영역에서 구한 값을 비교하여 둘중 작은 것을 선택한다. 이를 분할정복하여 재귀를 통해 구하면 됌.
# 문제는 영역을 나눈 기준임. 

stars.sort() # x 좌표 순서로 정렬해보자

def search(left,right): # 이진 탐색을 통해 찾는 함수. 좌표가아니라 index를 이진탐색 할 예정. 좌표하니까 너무더러워짐
    if left == right: # 왼쪽 오른쪽이 같으면 이진탐색 종료한다. 같으면 점은 1개니까. 
        return
    
    if right - left == 1: # 점 2개남았으니 두 점 사이 거리가 그 범위에서 가장 작은 두점사이의 거리임
         a = stars[right][0]-stars[left][0]
         b = stars[right][1]-stars[left][1]
         return a*a + b*b
    
    # 여기부터는 left,right 사이에 점이 2개 이상이라는 뜻.
    mid = (left+right)//2 # 가운데 설정
    min_val = min(search(left,mid),search(mid,right)) # 가운데를 기준으로 좌,우로 나누어서 각각에서 구한 가장 작은 두점사이의 거리끼리 비교. 현재 left,right 범위 내에서 x좌표를 기준으로 이웃하는 점과의 거리들 중에서 가장 작은 애가 나옴. 최솟값으로 우선 설정해주자
    #하지만 가장 가까운 두 점이 이웃하리라는 보장은 없음. 2차원이기 때문에.

    #이제 mid와 가장 가까운애를 구해본다. 그 후 위에서 구한 최솟값과 비교해야함.
    #왜 mid를 기준으로할까? 위에서 재귀를 타게 되므로 mid는 좌우로 각각 이동하게됨.
    #따라서 모든 점 간의 거리 비교는 한 점이 미드가 되었을 때 발생한다고 볼 수있음.
    # 예를 들어, 1~10 범위라면 mid인 5를 기준으로 1-5,2-5,3-5,..,10-5 을 보게된다.
    # 그럼 2-3의 경우는 어떻게 확인할까
    # 위 26번행에서 재귀를 탔으니 다음 은 1~5 와 5~10 범위에서 함수가 호출된다.
    # 각각 mid가 3,7 이니 함수 내부에서 1-3,2-3,4-3,5-3 을 비교하게 될것.
    # 이렇게 모든 점간의 비교는 발생한다. 둘 중 한 점이 언젠가 mid가 될 수밖에 없기 때문 

    new_stars = [] # 모든 점을 다 볼 필요 없이 범위에 맞는 애만 볼 예정. 시간초과땜시..
    for i in range(left,right+1): # left,right는 index니까 right-1 이 아니라 right까지 반복해야함
        if (stars[mid][0]-stars[i][0])**2 < min_val: # mid와 후보 사이의 x좌표 거리의 제곱이 현재 최솟값을 넘으면 걔는 볼 필요도 없음
            new_stars.append(stars[i]) # 안넘는 애만 새로운 리스트에 담는다.
    
    new_stars.sort(key=lambda x:x[1]) # 남은애들을 이제 y좌표로 정렬
    k = len(new_stars) # n은 이전의 길이니까 새 길이 변수 설정
    for i in range(k-1):
        for j in range(i+1,k):
            if (new_stars[j][1]-new_stars[i][1])**2 < min_val: # 마찬가지로 두 점사이의 y좌표 거리의 제곱이 최솟값 넘으면 볼 필요 없음
               tmp = (new_stars[j][1]-new_stars[i][1])**2 + (new_stars[j][0]-new_stars[i][0])**2 #볼 필요 있는애만 실제 거리 구해보자
               min_val = min(min_val,tmp) #위에서 구한 최솟값과 비교하여 업데이트
            # y좌표를 기준으로 정렬되있음. i,j의 y좌표 거리의 제곱이 최솟값을 넘으면 j가 다음 index를 가르키는건 계산해봤자 의미없음. y좌표 거리는 더 멀어지기 때문에 어차피 제곱해봤자 최솟값 넘는건 당연함. 따라서 새로운 i를 설정해서 후보를 탐색하는게 시간낭비를 줄일 수 있음.
            else: 
                break
    return min_val
ans = search(0,n-1)
print(ans)