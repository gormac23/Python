def is_prime(n, a=2):
    if n < a:
        return False
    elif n == a:
        return True
    elif n % a == 0:
        return False
    else:
        return is_prime(n,a+1)