# Given an integer N, print the following pattern :

5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5


# Outer loop for row 
n=5 
for i in range(2 * n - 1):
            # Inner loop for columns
    for j in range(2 * n - 1):
                # Calculate distance from top
        top = i
                # Calculate distance from left
        left = j
                # Calculate distance from bottom
        bottom = (2 * n - 2) - i
                # Calculate distance from right
        right = (2 * n - 2) - j

                # Take the minimum of all four distances
        minDist = min(top, bottom, left, right)

                # Print number (starts with n at border, decreases inside)
        print(n - minDist, end=" ")
            # Move to the next row
    print()
