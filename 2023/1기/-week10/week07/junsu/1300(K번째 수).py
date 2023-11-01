import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
left = 1
right = n**2

while left<=right:
    tmp = 0
    mid = (left+right)//2
# 아랫부분에 대한 설명
# tmp는 어떤 수보다 작은 것의 갯수를 세기 위해 설정한 것임
# 1행은 1,2,3,4,5,... 구구단 1단
# 2행은 2,4,6,8,10,... 구구단 2단
# n행은 n,2n,3n,4n,5n,... 구구단 n단
# mid를 i로 나누면 각 행에서 mid보다 작은 수의 갯수를 구할수 있음.
# mid가 6이라면 6//1 = 6, 6//2 = 3, 6//3 = 2, 6//4 = 1, 6//5=1 ,6//6=1, 6//7=0
# 즉 1행에는 6개, 2행에는 3개, 3행 2개, 4행과 5행,6행은 1개 그이후에는 mid보다 작은 수 없음
# 1행부터 n행까지 이 모든 수를 더하면 이 2차원배열에 mid보다 작은 값을 가진 수의 갯수가 나옴
# 2차원 배열의 모든 수를 일렬로 정렬한것이 B이므로 같은 의미임
# tmp를 이분탐색을 이용해 k를 찾으면 된다.
    for i in range(1,n+1):
        tmp += min(mid//i,n)
    if tmp >= k:
        right = mid - 1
        ans = mid
        
    else:
        left = mid + 1

print(ans)
