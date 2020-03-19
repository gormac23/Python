'''
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

### BELOW CODE FROM PROBLEM 3 ###

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
    while (i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i += 6

    return True


def prime_factors(n) :
    
    # Check base case: if n itself is prime
    if (is_prime(n)) :
        return [n]

    factors = []    # list to store prime factors
    div = 2         # divisor
    new_num = n     #

    while (div <= n) :
        # if divides evenly and is prime, store div and decrease new_num
        if (new_num % div == 0 and is_prime(div)) :
            factors.append(div)
            new_num /= div
        else:
            div += 1

    return factors


def count(l) :

     # Count the amount of repeated primes store vals to dict
    primes = dict()
    for i in l :
        primes[i] = primes.get(i, 0) + 1

    return primes


def main() :

    lcm = 1
    # Create dictionary of all primes < 20
    powers = {x:0 for x in range(20) if is_prime(x)}

    # Creates dictory of prime factors for every number from 2-20
    for x in range(2, 21) :
        factors = count(prime_factors(x))

        # Then compaares the amount with the current highest number of primes
        for key in factors :
            if powers[key] < factors[key] :
               powers[key] = factors[key]

    # Calculate the lowest common multiple
    for key in powers :
        lcm *= key ** powers[key]

    print(lcm)


if __name__ == '__main__':
    main()