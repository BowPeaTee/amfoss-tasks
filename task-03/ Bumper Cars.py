X,N = map(int, input().split())
pos=list(map(float, input().split()))
dir=list(map(int, input().split()))
count,a=0,0
while a!=0:
    count+=0.5
    a=0
    #changing position by 0.5
    for i in range(X):
        if dir[i]==1:
            pos[i]+=0.5
        else:
            pos[i]-=0.5
    for i in pos:
        if (i*2)//1 in range(1,2*(N+1)):
            if i!=0:
                a+=1
    #checking if list elements are not unique
    if not(len(set(pos)) == len(pos)):
        for i in range(X):
            for j in range(i+1,X):
                if pos[i]==pos[j]:
                    dir[i]*=-1
                    dir[j]*=-1
                    break
print(int(count))