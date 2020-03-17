'''
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def multiple_3_and_5(n):
	total = 0
	for x in range(n):
		if x % 5 == 0 or x % 3 == 0:
			total += x
	return total

def main():
	print(multiple_3_and_5(1000))

if __name__ == '__main__':
	main()