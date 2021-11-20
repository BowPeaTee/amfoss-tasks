from math import sqrt
for t in range(int(input())):
    l=[]
    n=int(input())
    while n % 2 == 0:
        l.append(2),
        n = n // 2 
    for i in range(3,int(sqrt(n))+1,2):
        while (n % i == 0):
            l.append(i)
            n = n // i
    if n > 2:
        l.append(n)
    print(max(l))
    
