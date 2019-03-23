from subprocess import call #enables the ability to call other scripts

electrons = 'How many electrons? (0-20)' #defines a variable - electrons

endq = 'Do you want to do another? (y, n)' #defines a variable - endq

print(electrons) #writes the variable - electrons

number = raw_input() #defines a variable - number - as the user input to the question

number = int(number) #converts the user input from string to integer format - this allows the if functions to process it less funky

ones = 0 #defines a variable - ones

twos = 0 #defines a variable - twos

twop = 0 #defines a variable - twop

threes = 0  #defines a variable - threes

threep = 0  #defines a variable - threep

fours = 0  #defines a variable - fours

valence = 0  #defines a variable - valence



if number > 0: #function if user input is greater than 0

	ones += 1 #adds 1 to the value of the variable - ones
	
	valence = ones #sets the variable - valence - to the value of the variable - ones


#code is practially the same for a while

if number > 1:
		
	ones += 1
		
	valence = ones
				
if number > 2:
			
	twos += 1

	valence = twos + twop #resets the variable - valence - to the value of the orbitals of the outermost shell - twos 

if number > 3:

	#print 'yes'

	twos += 1
			
	valence = twos + twop

if number > 4:

	twop += 1

	valence = twos + twop

if number > 5:

	twop += 1
	
	valence = twos + twop
						
if number > 6:

	twop += 1
	
	valence = twos + twop
if number > 7:

	twop += 1

	valence = twos + twop

if number > 8:

	twop += 1
	
	valence = twos + twop
				
if number > 9:

	twop += 1
	
	valence = twos + twop

if number > 10:

	threes += 1

	valence = threes + threep

if number > 11:

	threes += 1

	valence = threes + threep

if number > 12:

	threep += 1

	valence = threes + threep
if number > 13:

	threep += 1

	valence = threes + threep
if number > 14:

	threep += 1

	valence = threes + threep
if number > 15:

	threep += 1

	valence = threes + threep
if number > 16:

	threep += 1

	valence = threes + threep
if number > 17:

	threep += 1

	valence = threes + threep
if number > 18:

	fours += 1

	valence = fours

if number > 19:

	fours += 1

	valence = fours

if number > 20 or number < 0: #function if user input is out of range 0-20
	
	call(["python", "electrons.py"]) #restarts the script




print str(valence) + ' valence' + '	1s^' + str(ones) + ' 2s^' + str(twos) + ' 2p^' + str(twop) + ' 3s^' + str(threes) + ' 3p^' + str(threep) + ' 4s^' + str(fours) #writes the electron configuration and valence electrons - 'str' must be put in front of each variable to tell the computor that the variable is in 'string' format

print(endq) #writes the variable - endq

endans = raw_input() #defines a variable - endans - as the user input to the question 

if endans is 'y': #function if user input is 'y'

	call(["python", "electrons.py"]) #restarts the script

if endans is 'n': #function if user input is 'n'

	call(["python", "atom.py"]) #runs the beginning script
else: 

	call(["python", "electrons.py"]) #restarts the script

