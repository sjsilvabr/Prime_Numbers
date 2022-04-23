import numpy as np

def prime_list(n=2):
    """Returns the list of prime numbers 'p <= n'
       Input: n > 1 (integer)
       Output: list"""

    if n < 2: return []
    
    narray = np.append([2], np.arange(start=3, stop=n+1, step=2))
    limit = int(np.sqrt(n))
    primes = []
    prime = narray[0]
    
    while prime <= limit:
        primes.append(prime)
        narray = narray[narray % prime !=0]
        prime = narray[0]

    return list(np.append(primes, narray))
