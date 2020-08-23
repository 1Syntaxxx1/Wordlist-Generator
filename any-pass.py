import sys
import itertools
import time

if sys.version_info[0] !=3:
	print('''--------------------------------------
	REQUIRED PYTHON 3.x
	use: python3 'any-pass.py'
--------------------------------------
			''')
	sys.exit()

print("Loading...\n")

#colours
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'


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

print("\nUsage: python3 any-pass.py\n\n")
print('''Help: First you input characters that should be in the password,
afterwards you state the amount of character(s) the password should contain.\n\n''')


def passgen(i):
    	num = input("amount of character(s) that password must consist of: ")
    	yield from itertools.product(*([i] * int(num)))

while True:
    a = input("\nDO YOU WANT TO QUIT [(y)es/(n)o]?")
    if a == "n":
	    print(f"{red}If [a] output will be added to the file\n", end="")
	    print(f"{red}If [w] output will be Overwrite the file\n", end="")
	    with open(input('\nname password file as example.txt: '), input('Do you want to add or write to a file [a/w]?')) as f:
		    for x in passgen(input("Input character(s) to be used in password: ")):
			    print(''.join(x), file=f)
			    for i in range(101):
				    time.sleep(0.01)
				    sys.stdout.write("\r%d%%" % i)
				    sys.stdout.flush()
    elif a == "y":
	    print("Bye!!!")
	    quit()
    else:
	    print("Invalid!!!")
	    exit()