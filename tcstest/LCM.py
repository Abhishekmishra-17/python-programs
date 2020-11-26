# Python program to find LCM of two numbers

# Recursive function to return gcd of a and b
def gcd(a,b):
	if a == 0:
		return b
	return gcd(b % a, a)

# Function to return LCM of two numbers
def lcm(a,b):
	return (a / gcd(a,b))* b

# Driver program to test above function
a = 15
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b))
'''
# Python Program to find LCM of n elements 

def find_lcm(num1, num2): 
	if(num1>num2): 
		num = num1 
		den = num2 
	else: 
		num = num2 
		den = num1 
	rem = num % den 
	while(rem != 0): 
		num = den 
		den = rem 
		rem = num % den 
	gcd = den 
	lcm = int(int(num1 * num2)/int(gcd)) 
	return lcm 
	
l = [2, 7, 3, 9, 4] 

num1 = l[0] 
num2 = l[1] 
lcm = find_lcm(num1, num2) 

for i in range(2, len(l)): 
	lcm = find_lcm(lcm, l[i]) 
	
print(lcm)  
'''
'''
# Python3 program to find LCM of array 
# without using GCD. 

# Returns LCM of arr[0..n-1] 
def LCM(arr, n): 
	
	# Find the maximum value in arr[] 
	max_num = 0; 
	for i in range(n): 
		if (max_num < arr[i]): 
			max_num = arr[i]; 

	# Initialize result 
	res = 1; 

	# Find all factors that are present 
	# in two or more array elements. 
	x = 2; # Current factor. 
	while (x <= max_num): 
		
		# To store indexes of all array 
		# elements that are divisible by x. 
		indexes = []; 
		for j in range(n): 
			if (arr[j] % x == 0): 
				indexes.append(j); 

		# If there are 2 or more array 
		# elements that are divisible by x. 
		if (len(indexes) >= 2): 
			
			# Reduce all array elements 
			# divisible by x. 
			for j in range(len(indexes)): 
				arr[indexes[j]] = int(arr[indexes[j]] / x); 

			res = res * x; 
		else: 
			x += 1; 

	# Then multiply all reduced 
	# array elements 
	for i in range(n): 
		res = res * arr[i]; 

	return res; 

# Driver code 
arr = [1, 2, 3, 4, 5, 10, 20, 35]; 
n = len(arr); 
print(LCM(arr, n)); 

'''
