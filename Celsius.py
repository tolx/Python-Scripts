#########################
# @program: Celsius.py	
# @Date: 01/14/16			
#########################

#!/usr/bin/python

def conversion(input):
	return (1.8*input) + 32

def main():
		print ("Celsius to Fahrenheit")
		choice = input("> ")
		print " %d Celsius is %d Fahrenheit." % (choice, conversion(choice)
	
if __name__ == "__main__":
		main()
