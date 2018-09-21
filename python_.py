#basic system commands to the program
import sys

#main function definition 
def main():
	"""output something combined with the input
	provided by the user
	"""
#print 'Hello, You are',
    
first_num = input('Provide first number ')
    
second_num = input('Then provide a number to add ')
    
total = float(first_num) + float(second_num)
    
print'Your total for {0} & {1} is {2} and running this script as '.format(first_num, second_num, total),sys.argv[1]

if __name__ == '__main__':
	#call the function
	main()
