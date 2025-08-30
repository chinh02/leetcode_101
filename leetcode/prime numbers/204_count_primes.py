# Given an integer n, return the number of prime numbers that are strictly less than n.

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

n = 10

def countPrimes(n: int)-> int:
    p = 2
    sieve = [True] * (n+1)
    while p*p <= n:
        if sieve[p]:
            for i in range(p*p, n + 1 , p):
                sieve[i] = False
            p += 1
    result = 0
    for i in range(2,n+1):
        if sieve[i]:
            result += 1
    return result
print(countPrimes(n))