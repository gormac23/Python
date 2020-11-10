'''
This is my congruent calculator to help when
I am solving the Chinese Remainder Theorem
'''
from numpy import prod




def congruent(num,mod):
    i,ans = 0,0

    while ans != 1:
        i += 1
        ans = (num*i) % mod
        
    return i


def main():
    a_values = []
    N_values = []
    n_values = []
    x_values = []

    print("\n~.~ Welcome to the CTR calculator ~.~\n\nEnter number of equations 1, 2 or 3\n(Enter 1 for Multiplicative Inverse)")
    no_of_equations = input()

    if no_of_equations == "1":
        print("\nEnter Multiplicative Inverse as: a/b\u0025c")
        eqn = input().split("/")
        num = int(eqn.pop(0))
        # eqn = eqn.split("%")
        eqn = eqn[0].split("%")
        N = int(eqn.pop())
        a = int(eqn.pop())

        mi = congruent(a, N)
        print(f"\n\nThe Multiplicative Inverse of {a} is {mi}")
        print(f"and answer to {num}/{a}(mod {N}) = {num} x {mi}(mod {N}) = {num*mi%119}\n")
    
    # Using 2 equations
    elif no_of_equations == "2" or no_of_equations == "3":
        print("Now enter equation(s) as 'a\u0025b'\n")
        i = 0
        while i < int(no_of_equations):
            # Stores each number and modulo of input
            eqn = input().split("%")
            n_values.append(int(eqn.pop()))
            a_values.append(int(eqn.pop()))

            i += 1
        print("\n")
        aNx_values = []
        total_n = prod(n_values)

        for i in range(len(a_values)):
            # Pop first value of n to find N1, (the product of other modulos when 3 eqn)
            temp_N = n_values.pop(0)
            N_values.append(prod(n_values))

            # Find value that is equal to N1 congruent 1(mod n1)
            x_values.append(congruent(N_values[i], temp_N))

            # Find a * N * x for each iteration
            aNx_values.append(a_values[i] * N_values[i] * x_values[i])

            # String Format to display table of outputs
            if(no_of_equations == "2"):
                print(f"{a_values[i]:^3}| {n_values[0]:^2} | {N_values[i]} \u2245 1(mod {temp_N}) = {x_values[i]:<2} | {a_values[i]:>2} x {N_values[i]} x {x_values[i]:<2} = {aNx_values[i]}")
            else:
                print(f"{a_values[i]:^3}| {n_values[0]:^2} x {n_values[1]} = {N_values[i]} | {N_values[i]} \u2245 1(mod {temp_N}) = {x_values[i]:<2} | {a_values[i]:>2} x {N_values[i]} x {x_values[i]:<2} = {aNx_values[i]}")
            
            # Add temp N value back to end of list, changing the leading value to calculate next N value in loop
            n_values.append(temp_N)

        # Printing out final values
        total_aNx = sum(aNx_values)
        print(f"\n N  = {total_n:<}\naNx = {total_aNx:<}")
        print(f"\n{total_aNx}(mod {total_n}) = {total_aNx%total_n}\n\n")

    else:
        print("Invalid number of equations. Pick 1, 2 or 3")



if __name__ == '__main__':
    main()