# Insertion sort is a simple sorting algorithm that builds the sorted list one element at a time

# It works like sorting playing cards in your hand: you pick one card and place it in its correct position among the already sorted cards

def insertion_sort_swap(arr):
    n = len(arr)

    for i in range(1, n):
        j = i

        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return arr


numbers = [64, 25, 12, 22, 11]
print(insertion_sort_swap(numbers))
