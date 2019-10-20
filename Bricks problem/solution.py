n=int(input("enter the number of bricks :"))
def breakd(n):
    f=1
    a=0
    c=0
    for i in range(0,n):
        if(n==0):
            break
        else:
            n=n-f
            f=f+1
            if(n==0 or n<0):
                a=a+1
                return a
                break
            else:
                for j in range(0,2*i+2):
                    n=n-1
                    if(n==0 or n<0):
                        c=c+1
                        break

l=breakd(n)       
if(l):
    print("ram")
else:
    print("shayam")


