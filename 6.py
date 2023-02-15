a = input().split()
b = input().split()
s=""
for i in a:
    if i not in b:
        s+=i+", "
        #print(i,end=",")
for j in b:
    if j not in a:
        s+=j+", "
        #print(j,end=",")
print(s[:len(s)-2])        

#learn programming at includehelp
#learn python programming language
