from math import sqrt
a=int(input("enter the number want to be prime factor:"))
'''def pf(a):
    x=2
    if(a<=1):
        print("please enter the valid input")
    else:
        print("The prime factor of given numbere is \n")
        while(x<=a):
            if(a%x==0):
                print(x,end=" ")
                a//=x
            else:
                x+=1
'''
def pf(a):
    if(a<=1):
        print("please enter the valid input")
    else:
        while(a%2==0):
            print(2,end=" ")
            a=a//2
        for i in range(3,int(sqrt(a))+1,2):
            while(a%i==0):
                print(i,end=" ")
                a=a//i
        if(a>2):
            print(a)
pf(a)
