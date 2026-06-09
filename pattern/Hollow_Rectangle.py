# Given an integer N, print the following pattern : 

*****
*   *
*   *
*   *
*****


# Outer loop for rows
n=5
for i in range(n):
            # Inner loop for columns
    for j in range(n):
                # Print star if it's a border cell
        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                    print("*", end="")
                # Print space otherwise
        else:
                    print(" ", end="")
            # Move to next line after each row
    print()
