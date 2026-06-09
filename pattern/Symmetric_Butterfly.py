# Given an integer N, print the following pattern :
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *


# Initialize spaces between star blocks
n=5
spaces = 2 * n - 2

        # Loop for rows
for i in range(1, 2 * n):
            # Calculate stars for first half
            stars = i

            # Adjust stars for second half
            if i > n:
                stars = 2 * n - i

            # Print left stars
            print("*" * stars, end="")

            # Print spaces
            print(" " * spaces, end="")

            # Print right stars
            print("*" * stars)

            # Adjust spaces for next row
            if i < n:
                spaces -= 2
            else:
                spaces += 2
