for pwd in input().split(','):
    alpha = [chr(j) for j in range(97,123)]
    alphaCap = [j.upper() for j in alpha]
    digit = [str(j) for j in range(10)]
    special = ['!','@','#','$','^','&','%','*','(',')','_','-','+','=']
    flag_alpha, flag_alphaCap, flag_digit, flag_special = False, False, False, False
    if (len(pwd)>=6 and len(pwd)<=12):
        for i in pwd:
            if i in alpha and flag_alpha==False :
                flag_alpha = True
            if i in alphaCap and flag_alphaCap == False:
                flag_alphaCap = True
            if i in digit and flag_digit==False:
                flag_digit = True
            if i in special and flag_special == False:
                flag_special = True
    if (flag_alpha and flag_alphaCap and flag_digit and flag_special):
        print(pwd,sep=',')


#ABd1234@1,aF1#,2w3E*,2We3345        
