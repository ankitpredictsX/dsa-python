def check_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

arr = [1, 2, 3, 4, 5]

print(check_sorted(arr))

#Short Python method

arr = [1, 3, 5, 4, 2]

print(arr == sorted(arr))
