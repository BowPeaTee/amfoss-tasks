def func(n):
    n=float(n)
    n=abs(n)
    return(n)
t=int(input())
l=[]
for i in range(t):
    marx=0
    n,k=map(int,input().split())
    if k!=0:
        marx=max(list(map(func,input().split())))
    else:
        marx=max(list(map(float,input().split())))
    l.append(marx)
for i in l:
    print(i)
