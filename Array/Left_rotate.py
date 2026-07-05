# Using Slicing
def left_rotate_by_d(arr, d):
    n = len(arr)

    if n == 0:
        return arr

    d = d % n

    return arr[d:] + arr[:d]


arr = [1, 2, 3, 4, 5]
d = 2

print(left_rotate_by_d(arr, d))

# Without Slicing
def left_rotate_by_d(arr, d):
    n = len(arr)

    if n == 0:
        return arr

    d = d % n

    temp = []

    for i in range(d):
        temp.append(arr[i])

    for i in range(d, n):
        arr[i - d] = arr[i]

    for i in range(d):
        arr[n - d + i] = temp[i]

    return arr


arr = [1, 2, 3, 4, 5]
d = 2

print(left_rotate_by_d(arr, d))
