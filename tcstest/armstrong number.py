a=int(input("enter the number want to be checked :"))
def arms(a):
    rep=a
    c=len(str(a))
    s=0
    while(a>0):
        b=a%10
        a=a//10
        s=s+pow(b,c)
    if(s==rep):
        return("Arm")
    elif(s!=rep and type(rep)==int):
        return " no arm"
    else:
        print("invaild input")
        
print(arms(a))















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































