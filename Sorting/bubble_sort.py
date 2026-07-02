# Bubble sort is a simple sorting algorithm that repeatedly compares two adjacent elements and swaps them if they are in the wrong order.

# It is called bubble sort because the largest element slowly “bubbles up” to the end of the list after each pass.

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping happened, the list is already sorted
        if not swapped:
            break

    return arr


numbers = [5, 3, 8, 4, 2]
print(bubble_sort(numbers))
