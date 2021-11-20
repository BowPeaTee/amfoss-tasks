for i in range(int(input())):
    N=int(input())
    f,s=5,8
    sum=10
    while N>f+s:
        third=f+s
        if third%2==0:
            sum+=third
        f,s=s,third
    print(sum)
