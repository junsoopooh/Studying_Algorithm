import sys

n = int(sys.stdin.readline())
stars = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    stars.append([a,b])

stars.sort() # x좌표 기준 정렬
min_val = (stars[-1][0] - stars[0][0])**2 + (stars[-1][1] - stars[0][1])**2 # 가장 먼놈간의 거리의 제곱을 최솟값으로 설정

for i in range(n-1):
    for j in range(i+1,n):
        a = stars[j][0] - stars[i][0]
        if a*a >= min_val: # x좌표 만으로도 최소거리 넘어버리면 더이상 계산 무의미
            continue
        b = stars[j][1] - stars[i][1]
        tmp = a**2 + b**2
        min_val = min(min_val, tmp) # 둘중 작은 값 저장

stars.sort(key=lambda x : x[1]) # y좌표 기준 정렬

for i in range(n-1):
    for j in range(i+1,n):
        a = stars[i][0] - stars[j][0]
        if a*a >= min_val: # x좌표 만으로도 최소거리 넘어버리면 더이상 계산 무의미
            continue
        b = stars[i][1] - stars[j][1]
        tmp = a*a + b*b
        min_val = min(min_val,tmp)

print(min_val)