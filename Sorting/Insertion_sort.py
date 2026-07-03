# Insertion sort is a simple sorting algorithm that builds the sorted list one element at a time

# It works like sorting playing cards in your hand: you pick one card and place it in its correct position among the already sorted cards

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key at its correct position
        arr[j + 1] = key

    return arr


numbers = [5, 3, 8, 4, 2]
print(insertion_sort(numbers))
