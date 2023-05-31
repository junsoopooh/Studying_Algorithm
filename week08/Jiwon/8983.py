import sys
input = sys.stdin.readline

# 사대 수 m, 동물 수 n, 사정거리 l
m, n, l = map(int, input().split())

# 사대 리스트
peoples = list(map(int, input().split()))
peoples.sort()

# 동물 리스트
animals = [list(map(int, input().split())) for _ in range(n)]

# 사대는 x 좌표만, 동물은 x/y 좌표 둘 다 가지고 있으니
# 사대 리스트를 컨트롤하는 게 쉽겠군

count = 0

# "동물은 고정", 사대를 추적하면서 해당 동물을 잡을 수 있냐 없냐를 판별
for animal in animals:
    # 사대를 이분탐색
    left = 0
    right = m-1

    while left <= right:
        mid = (left + right) // 2

        minlocation = animal[0] + animal[1] - l
        maxlocation = animal[0] - animal[1] + l

        # 동물을 잡을 수 있는 범위 안에 있는지 확인
        if minlocation <= peoples[mid] and peoples[mid] <= maxlocation:
            # 잡았네? 카운팅하고 나가야지
            count += 1
            break
        elif minlocation > peoples[mid]:
            left = mid + 1
        else:
            right = mid - 1

print(count)