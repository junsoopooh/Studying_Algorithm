import sys

n = int(sys.stdin.readline())
arr = set() # 겹치는 단어를 제거하기 위해 set로 설정
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    arr.add(word) # set의 operation인 add 사용

arr = list(arr) # 다시 list로 변환

data = [[] for _ in range(50)] # 단어 길이는 최대 50이다. 각 단어는 (자신의 길이)-1 을 index로 하는 리스트에 삽입된다.

for i in arr:
    l = len(i) # 자신의 길이
    data[l-1].append(i) # data의 index는 0~49이므로 1 빼준다.
    data[l-1].sort() # 단어가 들어간 리스트는 모두 같은 길이이므로 알파벳 순으로 정렬해준다.

for x in data:
    if x: # 리스트가 비어있지 않다면 출력
        for y in x: 
            print(y, end='\n')
