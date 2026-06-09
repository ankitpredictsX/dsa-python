# Given an integer N, print the following pattern :
A 
A B 
A B C 
A B C D 
A B C D E

 # Outer loop for the number of rows
for i in range(5):
            
        # Inner loop to print alphabets from A to A + i
        for j in range(i + 1):
            print(chr(65 + j), end=" ")  # Print the alphabet character followed by a space

        # Move to the next line after printing the current row
        print()
