size= int(input("Pleae enter the size of array:"))
print("Enter the elements of array.....")
b=[]
x=0
for i in range(0,size):
    a=int(input("Enter the "+str(i)+"th element:"))
    b=b+[a]
key=int(input("Enter the number want to be search:"))
for i in range(0,size):
    if(key==b[i]):
       x= print("The item "+str(key)+" is found at the location",i)
if(x!=0):
    print("")
else:
    print("Item dosen't found")
