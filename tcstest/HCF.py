# Recursive function to return gcd of a and b
def gcd(a,b):
	
	# Everything divides 0 
	if (a == 0):
		return b
	if (b == 0):
		return a

	# base case
	if (a == b):
		return a

	# a is greater
	if (a > b):
		return gcd(a-b, b)
	return gcd(a, b-a)

# Driver program to test above function
a = 3
b = 51
if(gcd(a, b)):
	print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
	print('not found')
    
'''
# GCD of more than two (or array) numbers

# Function implements the Euclidian 
# algorithm to find H.C.F. of two number
def find_gcd(x, y):
	
	while(y):
		x, y = y, x % y
	
	return x
		
# Driver Code	 
l = [2, 4, 6, 8, 16]

num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1, num2)

for i in range(2, len(l)):
	gcd = find_gcd(gcd, l[i])
	
print(gcd)
'''
