# Given an integer N, print the following pattern :

1     1
12   21
123 321
12344321


for i in range(1,5):
    for j in range(1,i+1):
        print(j,end='')
    for k in range(1,2*(4-i)):
        print(" ",end='')
    for m in range(i,0,-1):
        print(m,end='')
    print()
