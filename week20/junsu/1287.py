import sys

s = list(sys.stdin.readline().rstrip())
arr = []
tmp = []
for i in range(len(s)):
    if s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
        if not tmp:
            ans = 'ROCK'
            break
        num = ''.join(tmp)
        arr.append(num)
        tmp = []
    else:
        tmp.append(s[i])
print(s)
