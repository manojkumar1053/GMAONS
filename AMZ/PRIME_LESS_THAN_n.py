def prime(n):
    #primeNumber = []
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    primeNumber = [2] + [i for i in range(3, n, 2) if sieve[i]]
    return len(primeNumber)


print(prime(10))
