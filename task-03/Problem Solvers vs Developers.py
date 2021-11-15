import sys
n,m = map(int, input().split())
if n>m:
    print('NO')
else:
    nlist=sorted(map(int,input().split()))
    mlist=sorted(map(int,input().split()))
    if (max(nlist) and max(mlist) > 100) or (min(nlist) and min(mlist) < 1):
        sys.exit() 
    sum,prevsum=0,0
    for i in nlist:
        for j in mlist:
            if j-i>0:
                sum+=j
                mlist.remove(j)
                break
        if (sum-prevsum)==0:
            print('NO')
            break
        prevsum=sum
    else:
        print("YES")
        print(sum)        