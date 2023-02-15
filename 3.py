n = int(input())
k = int(input())
arr=[]
for i in range(n):
    s = []
    for j in range(k):
        s.append(i*j)
    arr.append(s)
print(arr)

#n=3
#k=5
