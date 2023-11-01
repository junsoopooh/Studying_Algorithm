import sys

word = sys.stdin.readline().rstrip()
stk = []
tmp = 1
ans = 0

for i in range(len(word)):
    if word[i] == '(':
        stk.append('(')
        tmp *= 2

    elif word[i] == '[':
        stk.append('[')
        tmp *= 3

    elif word[i] == ')':
        if not stk or stk[-1] != '(':
            ans = 0
            break

        if word[i-1] == '(':  # 여기를 stk[-1]과 word[i-1]로 하냐에 따라 달라진다.
            ans += tmp
        tmp //= 2
        stk.pop() 
          
    elif word[i] == ']':
        if not stk or stk[-1] != '[':
            ans = 0
            break
        
        if word[i-1] == '[': # 여기를 stk[-1]과 word[i-1]로 하냐에 따라 달라진다.
            ans += tmp
        tmp //= 3
        stk.pop()
        

if stk:
    print(0)
else:
    print(ans)