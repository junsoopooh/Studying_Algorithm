numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    N = len(numbers)
    sums = []

    def recursion(cur_index, cur_sum):
        if cur_index == N:
            if cur_sum == target:
                sums.append(cur_sum)
            return
        else:
            recursion(cur_index+1, cur_sum+numbers[cur_index])
            recursion(cur_index+1, cur_sum-numbers[cur_index])

    recursion(0, 0)
    answer = len(sums)
    return answer

print(solution(numbers, target))