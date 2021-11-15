N=int(input())
l=[]
l=list(map(int,input().split()))
sum=0
sums=[]
for i in range(int(input())):
    a,b=map(int,input().split())
    for x in range(a-1,b):
        sum+=l[x]
    sums.append(sum)
    sum=0
for i in sums:
    print(i)