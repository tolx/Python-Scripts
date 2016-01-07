#########################
# @program: metric.py	
# @contributers: 
# @Date: 01/06/16			
# Metric system...			
#########################

#!/usr/bin/python

def main():
	print ("Metric System Conversion")
	metrics = ["Inches", "Centimeters"]
	
	print ("Your Options: ")
	# taverse through list
	for dispMetrics in metrics:
		print ("%s") % dispMetrics

	# ask for user input
	print ("What would you like to convert?")
	choice = input("> ")

if __name__ == "__main__":
	main()
