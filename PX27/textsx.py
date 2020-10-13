str1 = "abcde"
str2 = "abcxyz"
lcs = [[[] for row in range(len(str1) + 0)] for column in range(len(str2) + 0)]
print(lcs)
print("column: ", len(lcs))
print("row: ", len(lcs[0]))

print([[i for i in range(1, 6)] for j in range(1, 3)])
