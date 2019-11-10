import math
a=float(input("enter the cofficient of x^2:"))
b=float(input("enter the cofficient of x:"))
c=float(input("enter the contant:"))
if(a==0):
    print("equation is not quadratic...")
elif((pow(b,2)-(4*a*c))==0):
    x=-b/(2*a)
    print("First solution is:",x)
    print("second solution is:",x)
elif(((b**2)-(4*a*c))<0):
    d=pow((pow(b,2)-(4*a*c)),0.5)
    x=(-b)/(2*a)+ (d)/(2*a)
    y=(-b)/(2*a)-(d)/(2*a)
    print("First solution is:",x)
    print("second solution is:",y)
elif((pow(b,2)-(4*a*c))>0):
    d=pow((pow(b,2)-(4*a*c)),0.5)
    x=(-b)/(2*a)+ (d)/(2*a)
    y=(-b)/(2*a)-(d)/(2*a)
    print("First solution is:",x)
    print("second solution is:",y)
else:
    print("please enter the valid input..")

