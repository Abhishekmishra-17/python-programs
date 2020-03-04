size= int(input("Pleae enter the size of array:"))
print("Enter the elements of array without duplicated.....")
b=[]
for i in range(0,size):
    a=int(input("Enter the "+str(i)+"th element:"))
    b=b+[a]
key=int(input("Enter the number want to be search:")) 
def binarySearch (arr, l, r, x):  
    while r >= l: 
        mid = l + (r - l)//2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid+1, r, x)  
    return -1         
result = binarySearch(b, 0, len(b)-1, key) 
if result != -1: 
    print("Element is present at index %d" % result)
else: 
    print("Element is not present in array")
