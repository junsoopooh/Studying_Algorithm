strings = ["abce", "abcd", "cdx"]
n = 2

def solution(strings, n):
    strings.sort()
    strings.sort(key = lambda x:x[n])

    return strings

print(solution(strings, n))