rows = 5
for i in range(rows+1):   
    print(" "*i,end="")
    for j in reversed(range(i+1,rows+1)):   
        print(j, end=" ")
    for l in range(i):
        print(' ', end=" ")
    for k in range(i + 1, rows+1):
        print(k,end=" ")
    print('\n')
