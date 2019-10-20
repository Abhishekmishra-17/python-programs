# Write a program(using recursion)which generates the factorial of a number.
n=input("Enter the number to find the factorial:")
fact=1

def fact_of_number(b,fact):
        if(b<0):
            print("Invalid number,please enter the valid number.")
        else:
            if b>0: 
               fact_of_number(b-1,fact*b)
            else:
               print("The factorial of given number is:",fact)
             
if(n.isdigit()):
    b=int(n)
    fact_of_number(b,fact)
else:
    print("Invalid input,please enter the valid number")
