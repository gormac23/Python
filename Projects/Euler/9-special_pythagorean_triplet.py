'''
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from math import sqrt


def pythagoras(n,m) :

    total = 0
    for b in range(n,m) :
        for a in range(1, b) :
            c = sqrt(a**2 + b**2)
            if c % 1 == 0 :
                total = int(a+b+c)
                if total == 1000 :
                    print(f"{a:>3} + {b:^3} + {int(c):^3} = {total}")
                # return(a, b, int(c))

def main() :

    pythagoras(100, 400)
    print(200*375*425)
    # for x in range(100,500) :
    #     if pythagoras(x) != None :
    #         print(pythagoras(x))




if __name__ == '__main__':
    main()
