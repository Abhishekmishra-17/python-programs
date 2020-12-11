size= int(input("Pleae enter the size of array:"))
print("Enter the elements of array.....")
b=[]
x=0
for i in range(0,size):
    a=int(input("Enter the "+str(i)+"th element:"))
    b=b+[a]
def bubbleSort(arr): 
    n = len(arr)  
    for i in range(n): 
        for j in range(0, n-i-1):  
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
bubbleSort(b) 
  
print ("Sorted array is:")
for i in range(len(b)): 
    print ("%d" %b[i],end=" ")
