  # 

def solution(str1, str2):
    def check(x):
        if len(x) < 2:
            return False
        if x[0].islower() and x[1].islower():
            return True
        else:
            return False

    str1 = list(str1)
    str2 = list(str2)
    arr1 = []
    arr2 = []
    for i in range(len(str1) - 1):
        if str1[i].isupper():
            str1[i] = str1[i].lower()
        if str1[i + 1].isupper():
            str1[i + 1] = str1[i + 1].lower()
        if check(str1[i] + str1[i + 1]):
            arr1.append(str1[i].lower() + str1[i + 1].lower())
    for i in range(len(str2) - 1):
        if str2[i].isupper():
            str2[i] = str2[i].lower()
        if str2[i + 1].isupper():
            str2[i + 1] = str2[i + 1].lower()
        if check(str2[i] + str2[i + 1]):
            arr2.append(str2[i].lower() + str2[i + 1].lower())
    arr_all = arr1 + arr2
    arr_set = set(arr_all)
    n_max = 0
    n_min = 0

    for i in arr_set:
        n_max += max(arr1.count(i), arr2.count(i))
        if i in arr1 and i in arr2:
            n_min += min(arr1.count(i), arr2.count(i))

    if str1 == str2:
        answer = 65536
    elif not n_max and not n_min:
        answer = -1
    else:
        answer = int((n_min / n_max) * 65536)
    return answer
