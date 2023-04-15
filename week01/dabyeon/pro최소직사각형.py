sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

def solution(sizes):
    re_sizes = []
    for size in sizes:
        re_sizes.append([min(size), max(size)])

    max_w = float('-inf')
    max_h = float('-inf')

    for w, h in re_sizes:
        max_w = max(max_w, w)
        max_h = max(max_h, h)

    return max_w*max_h