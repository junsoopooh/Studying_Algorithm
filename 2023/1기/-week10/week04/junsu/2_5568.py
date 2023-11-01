import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
cards = []
for _ in range(n):
    card = sys.stdin.readline().rstrip()
    cards.append(card)

ans = set()
if k == 2:
    for i in cards:
        for j in cards:
            if cards.index(i) != cards.index(j):
                new_word1 = ''.join([i,j])
                new_word2 = ''.join([j,i])
                ans.add(new_word1)
                ans.add(new_word2)
elif k == 3:
    for i in cards:
        for j in cards:
            if cards.index(i) != cards.index(j):
                for l in cards:
                    if cards.index(i) != cards.index(l) and cards.index(j) != cards.index(l):
                        new_word1 = ''.join([i,j,l])
                        new_word2 = ''.join([i,l,j])
                        new_word3 = ''.join([j,i,l])
                        new_word4 = ''.join([j,l,i])     
                        new_word5 = ''.join([l,i,j])
                        new_word6 = ''.join([l,j,i])
                        ans.add(new_word1)
                        ans.add(new_word2)
                        ans.add(new_word3)
                        ans.add(new_word4)
                        ans.add(new_word5)
                        ans.add(new_word6)

print(len(ans))