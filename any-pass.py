import sys, itertools, time, argparse

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
activities carried out using this password Generator.\n''')

def xdec(func):
    def addx(*args, **kwargs):
        print("                  ",("x"*35))
        func(*args, **kwargs)
        print("                  ",("x"*35), "\n")
    return addx


def odec(func):
    def addo(*args, **kwargs):
        print("                    ",("o"*35))
        func(*args, **kwargs)
        print("                    ",("o"*35))
    return addo

@xdec
@odec
def hip(x):
    print(x)

hip("                         WELCOME TO THE WORDLIST GENERATOR")

parser = argparse.ArgumentParser(description='This program was inspired by the wordlist generator \"CRUNCH\"!', usage='python/python3, %(prog)s, [option]', epilog='Thanks for your support!\n')
parser.add_argument("-i", "--info", help='Type \"Creator\" with -i =>> ')
argu = parser.parse_args()

if argu.info:
    print("This program was coded by ", end=" >> ")
    print("Syntaxxx\n")
    print("Telegram", end=" @")
    print("syntaxxxtechexpert")

print("\nUsage: python3 any-pass.py\n\n")
print('''Help: First you input characters that should be in the password,
afterwards you state the amount of character(s) the password should contain.\n\n''')


def passgen(i):
    	num = input("amount of character(s) that password must consist of: ")
    	if num == str:
                print("Invalid")
                exit()
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
