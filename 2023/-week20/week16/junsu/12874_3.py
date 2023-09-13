import sys

s = sys.stdin.readline().rstrip()
n = len(s)

def check(s):
    stk = []
    for i in s:
        if i == '(':
            stk.append(i)
        else:
            if not stk:
                continue
            stk.pop()
    return not stk

def count(s):
    arr = set()
    for start in range(n):
        open = 0
        close = 0
        word = ""
        for end in range(start, n):
            word += s[end]
            if s[end] == '(':
                open += 1
            else:
                close += 1

            # 올바른 괄호 문자열인 경우만 고려
            if open == close:
                if check(word):
                    arr.add(word)

    return len(arr)%1000000007

ans = count(s)
print(ans)