l=[]
input()
l=map(int,input().split())
l=sorted(l)
towers=[]
count=1
try:
    for i in range(len(l)):
        if l[i]==l[i+1]:
            count+=1
        else:
            towers.append(count)
            count=1
except IndexError:
    towers.append(count)
print(max(towers), len(towers))