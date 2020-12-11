size= int(input("Pleae enter the size of array:"))
print("Enter the elements of array.....")
b=[]
for i in range(0,size):
    a=int(input("Enter the "+str(i)+"th element:"))
    b=b+[a]
def mg(b,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[]
    R=[]
    for i in range(1,n1+1):
        L=L+[b[p+i-1]]
    for j in range(1,n2+1):
        R=R+[b[q+j]]
    L=L+[max(b)+1]
    R=R+[max(b)+1]
    i=0
    j=0
    for k in range(p,r+1):
        if(L[i]<=R[j]):
            b[k]=L[i]
            i=i+1
        else:
            b[k]=R[j]
            j=j+1
def mrgsrt(b,p,r):
    if(p<r):
        q=(p+r)//2
        mrgsrt(b,p,q)
        mrgsrt(b,q+1,r)
        mg(b,p,q,r)
mrgsrt(b,0,size-1)
print("Sorted array is:",b)
        
