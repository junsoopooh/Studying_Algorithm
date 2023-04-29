import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
cards = []
for _ in range(n):
    card = int(sys.stdin.readline())
    cards.append(card)
arr=[]
def draw(y, arr):
    x = cards.po
    arr.append(x)
    y -= 1
    if k != 0:
        draw(y,arr)
    else:
        return

new_arr=draw(k,arr)
ans = set()
for i in range(len(new_arr)):
    a = new_arr[i]
    new_arr.remove(a)
    for j in range(len(new_arr)):
        b = new_arr[j]
        new_word = ''.join(a+b)
        new_word_2= ''.join(b+a)
        ans.add(new_word)
        ans.add(new_word_2)
print(len(ans))