import math

def pi_to_n(n):
	return f"\nPi to {n} decimal place(s): {math.pi:.{n}f}"

def main():
	
	while True:

		try:
			n = int(input("\nHow many decimal places would you like to calculate Pi to? "))
			break
		except ValueError:
			print("Please enter a digit")

	print(pi_to_n(n),"\n")







if __name__ == '__main__':
	main()