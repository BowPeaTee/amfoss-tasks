for t in range(int(input())):
    n=int(input())
    for i in range(n-1,101100,-1):
        s=str(i)
        if s==s[::-1]:
            for j in range(100,1000):
                if i%j==0 and len(str(i/j))==3:
                    print(i)
                    break
