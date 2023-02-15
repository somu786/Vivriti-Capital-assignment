k = int(input())
s = input().split()
res=''
for i in s:
    if len(i)>k:
        res+=i+','
print(res[:len(res)-1])


#k=6
#s=learn programming at include help
