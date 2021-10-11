def swap(Arr):
    le=len(Arr)
    a=Arr[:le//2]
    b=Arr[le//2:]
    global L
    L=b+a
L=[1,2,3,4,5]
print(L)
swap(L)
print(L)
