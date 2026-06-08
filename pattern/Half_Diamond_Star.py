# Input Format: N = 6
 # Result:   
     *
     **
     *** 
     ****
     *****
     ******  
     *****
     ****
     ***    
     **
     *

for i in range(0, 5):
    for j in range(0,i+1):
        print('*', end='')
    print()
for i in range(0, 4):
    for j in range(i+1,5):
        print('*', end='')
    print()
