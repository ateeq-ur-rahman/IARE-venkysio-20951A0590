def sort(a,k):
    n=len(a)
    o=[0]*n
    c=[0]*10

    for i in range(0,n):
        ink=a[i]/k
        c[int(ink)%10]+=1
    for i in range(1,10):
        c[i]+=c[i-1]
    
    i=n-1
    while i>=0:
        ink=a[i]/k
        o[c[int((ink)%10)]-1]=a[i]
        c[int((ink)%10)]-=1
        i-=1
    i=0
    for i in range(0,len(a)):
        a[i]=o[i]
    
def radix(a):
    m=max(a)
    k=1

    while m//k>0:
        sort(a,k)
        k*=10
a=list(map(int,input().split()))
radix(a)

for i in range(len(a)):
    print(a[i],end=" ")
