def multiple_3_5(number=1000):
    m3 = 0.0
    m5 = 0.0
    for i in range(number):
        if i % 3 == 0:
            m3 += i
        if i % 5 == 0:
            m5 += i
    return m3, m5


print(multiple_3_5())
