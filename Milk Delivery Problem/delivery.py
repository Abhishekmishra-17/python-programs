print(" n=number of milk route \n p=daily packet limit \n f=fine to be paid for each packet above the limit")
d=0
arr=list(map(int,input("enter three number n,p and f \n").split()))
print(arr)
if(len(arr)>3):
    print("please enter valid input.")
else:    
    n=arr[0]
    p=arr[1]
    f=arr[2]
    mor=list(map(int,input("enter the morning delivery volume not more than "+str(arr[0])+"\n").split()))
    if(len(mor)>n):
        print("please enter valid delivery volume.")
    else:
        eve=list(map(int,input("enter the eve delivery volume not more than "+str(arr[0])+"\n").split()))
        if(len(eve)>n):
            print("please enter valid delivery volume.")
    for i in range(0,n):
        a=max(mor)
        b=min(eve)
        e=a+b
        if(e>p):
            c=(e-p)
            d=d+c*f
        else:
            c=0
        mor.remove(a)
        eve.remove(b)
    print(d)
