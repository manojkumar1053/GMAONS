def multiple_3_5(number=1000):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


print("code1: ", multiple_3_5())


def mul35sum(Number=1000):
    return sum(x for x in range(Number) if (x % 3 == 0 or x % 5 == 0))


print("code2: ", mul35sum())
