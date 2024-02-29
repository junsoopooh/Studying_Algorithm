def solution(s, skip, index):
    answer = []
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    n = len(alphabet)

    def check(num, x):
        idx = alphabet.index(x)

        while num:
            idx += 1
            if idx == n:
                idx = 0
            result = alphabet[idx]
            if result not in skip:
                num -= 1
        return result

    arr = list(s)
    for i in arr:
        answer.append(check(index, i))

    return "".join(answer)
