# Quick sort is a fast sorting algorithm that uses the divide and conquer technique.

# It works by choosing one element as a pivot, then placing smaller elements on the left side and greater elements on the right side.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


numbers = [5, 3, 8, 4, 2]
print(quick_sort(numbers))
