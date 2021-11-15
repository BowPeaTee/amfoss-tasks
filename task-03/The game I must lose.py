N,M = map(int,input().split())
if N and M not in range(1,1000001):
    print('Error: Constraints not followed.')
elif N%2!=0:
    print(0)
else:
    count=0
    list=[]
    for i in range(1,M+1):
        if i%2!=0:
            count+=1
            list.append(i)
    print(count)
    for i in list:
        print(i, end=' ')
    print()