string = input().split()
s=""
for i in string:
    if ord(i[0])>=97 and ord(i[0])<=122:
        s+=chr(ord(i[0])-32)
        s+=i[1:]
    elif ord(i[0])>=65 and ord(i[0])<=90:
        s+=chr(ord(i[0])+32)
        s+=i[1:]
print(s)

#Hello world
