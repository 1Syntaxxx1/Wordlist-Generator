import sys
import itertools

if sys.version_info[0] !=3: 
	print('''--------------------------------------
	REQUIRED PYTHON 3.x
	use: python3 'any-pass.py'
--------------------------------------
			''')
	sys.exit()

def will_end():
	raise SystemExit
	
print("To continue type yes and to quit press Ctrl/Command key + C\n")
input("Do you wanna continue? ")
print("Loading...\n")


print('''---------------------------------------------------------------------------
===========================================================================
              ████████████████████████████████████████
              ████████████████████████████████████████
              ██████▀░░░░░░░░▀████████▀▀░░░░░░░▀██████
              ████▀░░░░░░░░░░░░▀████▀░░░░░░░░░░░░▀████
              ██▀░░░░░░░░░░░░░░░░▀▀░░░░░░░░░░░░░░░░▀██
              ██░░░░░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░░██
              ██░░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░██
              ██░░░░░░░░░░░░░░░░░▄▀░█░░░░░░░░░░░░░░░██
              ██░░░░░░░░░░████▄▄▄▀░░▀▀▀▀▄░░░░░░░░░░░██
              ██▄░░░░░░░░░████░░░░░░░░░░█░░░░░░░░░░▄██
              ████▄░░░░░░░████░░░░░░░░░░█░░░░░░░░▄████
              ██████▄░░░░░████▄▄▄░░░░░░░█░░░░░░▄██████
              ████████▄░░░▀▀▀▀░░░▀▀▀▀▀▀▀░░░░░▄████████
              ██████████▄░░░░░░░░░░░░░░░░░░▄██████████
              ████████████▄░░░░░░░░░░░░░░▄████████████
              ██████████████▄░░░░░░░░░░▄██████████████
              ████████████████▄░░░░░░▄████████████████
              ██████████████████▄▄▄▄██████████████████
              ████████████████████████████████████████
              ████████████████████████████████████████



This Tool Is For Educational Purposes Only, I won't be held liable for any illegal
activities carried out using this password Generator.



                +WELCOME TO ^SYNTAXXX PASSGen^+
               + 000000000000000000000000000000+
             + 1111111111111111111111111111111111+
           + 22222222222222222222222222222222222222+
         + 333333333333333333333333333333333333333333+
       + 4444444444444444444444444444444444444444444444+
     + 55555555555555555555555555555555555555555555555555+
   + 666666666666666666666666666666666666666666666666666666+
 + 7777777777777777777777777777777777777777777777777777777777+
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
===========================================================================
---------------------------------------------------------------------------''')


def passgen(i):
    	print("If you want to quit the program, press CTRL + C")	
    	print("NUMBER ONLY!!!")
    	num = input("amount of char that password must consist of: ")
    	yield from itertools.product(*([i] * int(num)))

print("\nUsage: python3 any-pass.py\n\n")
print('''Help: First you input characters that should be in the password,
afterwards you state the amount of characters the password should contain.
You only get five(5) chances to input.\n\n''')

with open(input('name password file as *.txt: '), 'w') as f:
	for x in passgen(input("Input char to be used in pass: ")):
    		print(''.join(x), file=f)
print("Loading...\n")
print("Successfully created!!!")

with open(input('name password file as *.txt: '), 'w') as f:
	for x in passgen(input("Input char to be used in pass: ")):
    		print(''.join(x), file=f)
print("Loading...\n")
print("Successfully created!!!")

with open(input('name password file as *.txt: '), 'w') as f:
	for x in passgen(input("Input char to be used in pass: ")):
    		print(''.join(x), file=f)
print("Loading...\n")
print("Successfully created!!!")

with open(input('name password file as *.txt: '), 'w') as f:
	for x in passgen(input("Input char to be used in pass: ")):
    		print(''.join(x), file=f)
print("Loading...\n")
print("Successfully created!!!")

with open(input('name password file as *.txt: '), 'w') as f:
	for x in passgen(input("Input char to be used in pass: ")):
    		print(''.join(x), file=f)
print("Loading...\n")
print("Successfully created!!!")

if (input("Type q to quit:") == "q"):
	will_end()



