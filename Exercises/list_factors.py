def list_factors(x):
    # We will store all factors in factors
    factors = []
    i = 1
    while i*i <= x:
        # Check if i divides x without leaving a remainder
        if x % i == 0:
            factors.append(i)
            # If it does, find the matching factor, i.e. how mnay times it divideds
            if x//i != i:
                factors.append(x//i)
        i += 1
    # Return the list of factors of x
    return factors


def main():
    factor = int(input("Enter number you want factor list of..."))
    print(list_factors(factor))


if __name__ == '__main__':
    main()