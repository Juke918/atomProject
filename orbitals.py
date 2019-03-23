from subprocess import call #enables the ability to call other scripts

 

start = "Which orbital? ('s', 'p', 'd')('n' to return to beginning)" #defines a variable - start

xyz = "Which Plane? ('x', 'y', 'z')" #defines a variable - xyz

print(start) #writes the variable - start

orbital = raw_input() #defines a variable - orbital - as the user input to the question 


if orbital is 's': #function if user input is 's'

	call(["python", "sorbital.py"])#runs the s orbital script

if orbital is 'p': #function if user input is 'p'

	print(xyz) #writes the variable - xyz

	plane = raw_input() #defines a variable - plane - as the user input to the question
	 
	if plane is 'y': #function if user input is 'y'
		
		call(["python", "yporbital.py"]) #runs the y p orbital script
	if plane is 'x': #function if user input is 'x'
		call(["python", "xporbital.py"]) #runs the x p orbital script
	if plane is 'z': #function if user input is 'z'
		call(["python", "zporbital.py"]) #runs the z p orbital script
	else:
		call(["python", "orbitals.py"])
	
if orbital is 'd': #funtion if user input is 'd'

	call(["python", "z2dorbital.py"]) #runs the d z2 orbital script

if orbital is 'n': #function if user input is 'n'

	call(["python", "atom.py"]) #runs the starting script

else: #function if user input is none of the above
	call(["python", "orbitals.py"]) #restarts this script

