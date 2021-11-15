n=int(input())
strn=input()
if strn==strn[::-1]:
    pass
else:
    for i in range(n//2):
        if strn[i]==strn[n-i-1]:
            continue
        else:
            for j in range(i+1,n-i):
                if strn[i]==strn[j]:
                    strn=strn[:j]+strn[n-i-1]+strn[j+1:n-i-1]+strn[j]
                    #strn[j],strn[n-i-1]=strn[n-i-1],strn[j]
            else:
                strn=strn.replace(strn[i],'',1)
print(n,'\n',strn)
