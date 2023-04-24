n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

# print(str(bin(22|14))[2:].zfill(n))

def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        bi_str = str(bin(arr1[i]|arr2[i]))[2:].zfill(n)
        # print(bi_str.replace("0", " ").replace("1", "#"))
        # bi_str.replace("0", " ").replace("1", "#")
        result.append(bi_str.replace("0", " ").replace("1", "#"))
    return result

print(solution(n, arr1, arr2))