x, y, w, h = map(int, input().split())
x_distance = min(x, abs(w-x))
y_distance = min(y, abs(h-y))
if x_distance < y_distance:
    print(x_distance)
else:
    print(y_distance)
print(min([x, y, w-x, h-y]))