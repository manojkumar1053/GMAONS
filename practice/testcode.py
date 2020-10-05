# capacity = 10
# items = 4
#
# kpc = [[0 for x in range(0, capacity + 1)]]
# kit = [[0] for y in range(0, items + 1)]
# kittest = [0 for y in range(0, items + 1)]
# print(kittest)
#
# kp_total = [[0 for x in range(0, capacity + 1)] for y in range(0, items + 1)]
#
# print("kpc", kpc)
# print("kit", kit)
# print(kp_total)
# print(items[2][2])
#
#


def prime(n):
    #primeNumber = []
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    primeNumber = [2] + [i for i in range(3, n, 2) if sieve[i]]
    return len(primeNumber)


print(prime(10))
