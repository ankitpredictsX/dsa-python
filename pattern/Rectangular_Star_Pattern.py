#Given an integer N, print the following pattern.
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

for i in range(0,5):
    print('* * * * *')
#or
for i in range(0,5):
    for j in range(0,5):
        print('*' ,end= ' ')
    print()
    
