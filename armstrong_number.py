#W.a.p.to find the given number is either armstrong number or not.
import math
A=int(input("Enter  number : "))
temp= A
B=A
n=0
s=0
while(A>0):
     S=A%10
     n=n+1
     A//=10
if(temp==0):
    n=1
print(n)
if(temp<0):
    print("The number is negative,please enter valid number")
while(temp>0):
       r=temp%10
       s+=math.pow(r,n)
       temp//=10
if(B==s):
    print("The given number",B,"is armstrong number.")
else:
    print("The given number ",B,"is not armstrong number.")

