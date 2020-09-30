"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

from functools import reduce


#
#
# def prime20(n=20):
#     lower = 2
#     upper = n
#     result = []
#     for number in range(lower, upper + 1):
#         if number > 1:
#             for i in range(2, number):
#                 if number % i == 0:
#                     break
#             else:
#                 result.append(number)
#     return reduce(lambda x, y: x * y, result)
#
#
# if __name__ == "__main__":
#     print(prime20())


# def prime20Solution2(n=20):
#     prime20 = []
#     for numberPrimeCheck in range(2, n + 1):
#         isPrime = True
#         for num in range(2, int(numberPrimeCheck ** 0.5) + 1):
#             if numberPrimeCheck % num == 0:
#                 isPrime = False
#                 break
#         if isPrime:
#             prime20.append(numberPrimeCheck)
#     return reduce(lambda x, y: x * y, prime20)
#
#
# if __name__ == "__main__":
#     print(prime20Solution2())
#
# import math
# def computeSum(n=20):
#     result = 1
#     x = [result*i//math.gcd(i,result) for i in range(1,n+1)]
#     return x
# print(computeSum())
