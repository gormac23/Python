'''
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def collatz_even(n):
    return n//2

def collatz_odd(n):
    return (3*n) + 1

def collatz_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2:
            n = collatz_odd(n)
            sequence.append(n)
        else:
            n = collatz_even(n)
            sequence.append(n)
    return sequence

def main():
    #Dictionary to store number as key and number of terms as value
    d = {}
    # Starts at one million
    for x in range(1_000_000, 0, -1):
        d[x] = len(collatz_sequence(x))

    # Find th elongest sequnce by getting the max value from dictionary
    # and returning the key associated with
    longest = max(d, key=d.get)
    print(longest)




if __name__ == '__main__':
    main()