#########################
# @program: metric.py	
# @contributers: 
# @Date: 01/06/16			
# Metric system...			
#########################

#!/usr/bin/python

def conversion(option1, option2):
	invalid = False
	if option1 == 1 and option2 == 2:
		value = int(input("inches = "))	
		ret = value*12
	elif option1 == 2 and option2 == 1:
		value = int(input("centimeters = "))
		ret = value / 12
	else:
		invalid = True
		print ("Invalid Input")

	# final result
	if not(invalid):
		print("result = %d" % ret)

def main():

		print ("Metric System Conversion")
		metrics = ["Inches", "Centimeters"]
	
		print ("Your Options: ")
	
		count = 0	
	
		# traverse through list
		for dispMetrics in metrics:
			count+=1
			print ("%d: %s" % (count, dispMetrics))

		# ask for user input
		print ("What would you like to convert?")
		choice = int(input(" Choice 1: "))
		choice2 = int(input(" Choice 2: "))
	
		conversion(choice, choice2)
		
		

if __name__ == "__main__":
		main()
		# Prompt if user would like to continue
		
			
