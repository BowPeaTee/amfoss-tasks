T=int(input())
for i in range(T):
    N=int(input())
    a=(N-1)//3
    b=(N-1)//5
    c=(N-1)//15
    ans=(a*(a*3+3)/2)+(b*(b*5+5)/2)-(c*(c*15+15)/2)
    print(int(ans))
