# Given an integer N, print the following pattern : 
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

for i in range(0,5):
    for j in range(1,5-i+1):
        print(j ,end= ' ')
    print()
    
