a=int(input("enter the index want to fabnocci series:"))
def feb(a):
    c=[0,1]
    if(a>2):
        for i in range(3,a+1):
            c=c+[c[i-2]+c[i-3]]
        return c
    elif(a==2):
        return c
    else:
        return [c[a-1]]
    
#print(str(feb(a)),end=" ")
s=feb(a)
for i in range(len(s)):
    print(s[i],end="   ")
