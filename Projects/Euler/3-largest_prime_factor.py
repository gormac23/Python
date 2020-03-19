

'''
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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

    while (div**2 <= n) :
        # if divides evenly and is prime, store div and decrease new_num
        if (new_num % div == 0 and is_prime(div)) :
            factors.append(div)
            new_num /= div
        else:
            div += 1

    return factors 


def main() :
    print(max(prime_factors(600851475143)))



if __name__ == '__main__':
    main()