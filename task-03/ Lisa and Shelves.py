from math import sqrt
n=int(input())
count=0
for i in range(1,int(sqrt(n))+1):
    if n%i==0:
        count+=1
        if n/i!=i:
            count+=1
print(count)