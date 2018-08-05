# Write your solution for 1.4 here!
def is_prime(x):
	for i in range(2,x):
		if x%i==0 :
		

			print("not a prim number")
			return(False)
			

	print("its a prim number")
	return(True)	
	


print(is_prime(5191))
