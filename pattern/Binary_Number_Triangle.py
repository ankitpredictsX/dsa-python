# Given an integer N, print the following pattern :
1
01
101
0101
10101

        # Loop over the number of rows
        for i in range(5):
            # If the row index is even, start with 1
            if i % 2 == 0:
                start = 1
            else:
                start = 0

            # Loop to print alternating 1's and 0's
            for j in range(i + 1):
                print(start, end="")
                # Alternate between 1 and 0
                start = 1 - start

            # Move to the next line after each row
            print()
