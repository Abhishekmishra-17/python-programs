'''Perfect number, a positive integer that is equal to the sum of its proper divisors.
The smallest perfect number is 6, which is the sum of 1, 2, and 3.
Other perfect numbers are 28, 496, and 8,128.'''


num=int(input("enter the number..."));
c=0
if(num>0):
    for i in range(1,num):
        d=num%i;
        if(d==0):
            c=c+i;
    if(c==num):
        print("perfect number\n");
    else:
        print("non-perfect number");

else:
    print("non-perfect number")

