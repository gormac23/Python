'''
Problem 15
Starting in the top left corner of a 2×2 grid,and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

# Number of routes using nCr, Choose combinations function
def choose(n,r):
    return factorial(n) // (factorial(r) * (factorial(n-r)))

def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

# Find the number of possibilites (routes) 
def main():
    grid_size = int(input("Square grid size ?\n" +
                          "(Enter one number. i.e 4, for 4x4 grid)\n"))

    # grid_size*2 represents the length * width
    print(f"No. of routes = {choose(grid_size*2, grid_size)}")




if __name__ == '__main__':
    main()