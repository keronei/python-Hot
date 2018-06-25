#basic system commands to the program
import sys

#main function definition 
def main():
	"""output something combined with the input
	provided by the user
	"""
	print 'Hello, You are',sys.argv[1]

if __name__ == '__main__':
	#call the function
	main()
