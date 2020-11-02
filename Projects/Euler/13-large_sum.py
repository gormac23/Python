'''
Problem 13
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''

def main():
    total = 0
    numbers = []
    i = 1
    with open("large_num.txt") as f:
        for line in f:
            # Take each line as input, strip whitespace,
            # convert to int and add to list of numbers to sum
            line = int(line.strip())
            numbers.append(line)
            
    # Convert the total sum of numbers to a string
    # In order to index the first ten digits
    total = str(sum(numbers))
    print(total[:10])



if __name__ == '__main__':
	main()