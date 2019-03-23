from subprocess import call #enables the ability to call other scripts

 

start = "Orbitals or Electrons? (o, e)" #defines a variable - start


print(start) #writes the variable - start

oe = raw_input() #defines a variable - oe - as the user input to the question 

if oe is 'o': #function if user input is 'o'

	call(["python", "orbitals.py"]) #runs the orbitals script

if oe is 'e': #function if user input is 'e'

	call(["python", "electrons.py"]) #runs the electrons script

else: #function if user input is none of the above
	
	call(["python", "atom.py"])#restarts the script


