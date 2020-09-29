"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""


#
# def longestPalindrome(m=100, n=100):
#     palindrome = []
#     for i in range(m, 1000, 1):
#         for j in range(n, 1000, 1):
#             x = i * j
#             lx = list(str(i * j))
#             if lx == lx[::-1]:
#                 palindrome.append(x)
#     return max(palindrome)

def longestPalindrome(m=100, n=100):
    return max([i * j for i in range(m, 1000) for j in range(n, 1000) if str(i * j) == str(i * j)[::-1]])


if __name__ == "__main__":
    print(longestPalindrome())
