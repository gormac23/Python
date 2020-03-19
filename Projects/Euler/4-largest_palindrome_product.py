'''
Problem 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def palindrome(n) :
	# Simple palindrome test
	test= str(n)
	return test == test[::-1]


def num_generator():
	# Starting two 3-digit numbers
	a = 999
	b = 999
	# Runs until palidrom is found
	while not palindrome(a*b):
		b -= 1
		# This checks 999 * 999-990 first and if it fails
		# a gets decreased and the process repeats for 998 * 999-990
		if str(b)[0:1] != str(a)[0:1]:
			b = a
			a -= 1

	print(f"{a} * {b} = {a*b} which is a palindrome")
	return a*b


def main() :

	print(palindrome(num_generator()))


if __name__ == '__main__':
	main()