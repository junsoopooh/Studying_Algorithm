import sys
input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    words.append(input().rstrip())

# words = ["but", "i", "wont", "hesitate", "no", "more", "no", "more", "it", "cannot", "wait", "im", "yours"]
words = list(set(words))
words.sort()
words.sort(key = lambda x: len(x))
print(*words, sep='\n')