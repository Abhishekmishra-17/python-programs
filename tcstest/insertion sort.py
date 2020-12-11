size= int(input("Pleae enter the size of array:"))
print("Enter the elements of array.....")
b=[]
for i in range(0,size):
    a=int(input("Enter the "+str(i)+"th element:"))
    b=b+[a]
for j in range(1,size):
    key=b[j]
    i=j-1
    while(i>-1 and b[i]>key):
        b[i+1]=b[i]
        i=i-1
    b[i+1]=key
print("sorted array is:",b)
    
