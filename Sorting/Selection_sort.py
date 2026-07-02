 #Selection sort is a simple sorting algorithm used to arrange elements in ascending or descending order.

#It works by repeatedly finding the smallest element from the unsorted part of the list and placing it at the correct position.

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        # find minimum element in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap current element with minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


nums = [64, 25, 12, 22, 11]
print(selection_sort(nums))
