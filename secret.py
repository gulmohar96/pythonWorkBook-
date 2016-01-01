#Python executes line by line, but the print statement inside teh function wont work unless teh function is called 
#when the functionis called, the statement will print first when the function is written in the code 
#
def secret(constant):
	print("never lost one min of sleeping", constant)
	return constant*5

sec = secret(2)

print(sec)

