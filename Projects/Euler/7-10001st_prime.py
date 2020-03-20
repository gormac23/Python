'''
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def is_prime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True

    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False

    i = 5
    while (i*i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i += 6
  
    return True

def main() :

	primes = [2]
	i = 3
	while len(primes) < 10001 :
		if is_prime(i) :
			primes.append(i)
			
		i += 2

	print(primes[-1])



if __name__ == '__main__':
	main()