import sys
sys.setrecursionlimit(10**9)

n, m = map(int, sys.stdin.readline().split())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
arr = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a-1, b-1))

tree = [[0, 0] for _ in range(4*n)]


def build_tree(idx, start, end):
    if start == end:
        tree[idx] = (nums[start], nums[start])
    else:
        mid = (start + end) // 2
        left = build_tree(2*idx+1, start, mid)
        right = build_tree(2*idx+2, mid+1, end)
        tree[idx] = min(left[0], right[0]), max(left[1], right[1])
    return tree[idx]


def query_tree(idx, start, end, a, b):
    if end < a or b < start:
        return (1e9, 0)
    if a <= start and end <= b:
        return tree[idx]

    mid = (start + end) // 2
    left = query_tree(2*idx+1, start, mid, a, b)
    right = query_tree(2*idx+2, mid+1, end, a, b)
    return min(left[0], right[0]), max(left[1], right[1])


build_tree(0, 0, n-1)
for a, b in arr:
    min_val, max_val = query_tree(0, 0, n-1, a, b)
    print(min_val, max_val)
