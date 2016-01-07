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
	
	count = 0	
	
	# traverse through list
	for dispMetrics in metrics:
		count+=1
		print ("%d: %s" % (count, dispMetrics))

	# ask for user input
	print ("What would you like to convert?")
	choice = input("> ")

if __name__ == "__main__":
	main()
