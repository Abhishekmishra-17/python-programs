''' Implementation of quick sort'''
size= int(input("Pleae enter the size of array:"))
print("Enter the elements of array.....")
b=[]
for i in range(0,size):
    a=int(input("Enter the "+str(i)+"th element:"))
    b=b+[a]
def partition(b,p,r):
    x=b[r]
    i=p-1
    for j in range(p,r):
        if(b[j]<=x):
            i=i+1
            temp=b[i]
            b[i]=b[j]
            b[j]=temp
    temp=b[i+1]
    b[i+1]=b[r]
    b[r]=temp
    return i+1
def qs(b,p,r):
    if(p<r):
        q=partition(b,p,r)
        qs(b,p,q-1)
        qs(b,q+1,r)
qs(b,0,size-1)
print("Sorted array is:",b)
                
