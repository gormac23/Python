'''
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

def list_of_digits(n,p):
    return [int(x) for x in str(n**p)]

def sum_list(l):
    return sum(l)

def main():
    num = 2
    power = 1000
    print(sum_list(list_of_digits(num, power)))



if __name__ == '__main__':
    main()

