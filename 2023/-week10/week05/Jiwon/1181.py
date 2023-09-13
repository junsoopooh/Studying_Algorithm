import sys
input = sys.stdin.readline

n = int(input())

words = set()
results = []

for _ in range(n):
    # 중복된 단어는 하나만 남기고 제거

    words.add(input().strip())

# 정렬기준: 길이가 짧은 것 -> 알파벳 순
results = list(words)
results.sort(key= lambda x: (len(x), x));

for result in results:
    print(result)