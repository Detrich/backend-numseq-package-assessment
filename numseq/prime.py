def primes(n):
    """returns a list of all primes less than n"""
    primesList = []
    sieve = [True] * (n+1)
    for p in range(2, n+1): #Used the Sieve of Eratosthenes to quickly sieve the primes
        if (sieve[p]):
            primesList.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return primesList



def is_prime(m):
    """Returns true or false depending on if the number is prime or not"""
    if m == 2:
        return True
    if m < 2:
        return False
    if not m & 1:
        return False
    for i in range(3, int(m**0.5)+1, 2):
        if m % i == 0:
            return False
    return True

