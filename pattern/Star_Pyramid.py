#Given an integer N, print the following pattern : 
    * 
   * * 
  * * * 
 * * * * 
* * * * *
  
for i in range(0, 5):
    # spaces
    for j in range(5, i, -1):
        print(' ', end='')
    # stars
    for k in range(0, i+1):
        print('*', end=' ')
    print()
