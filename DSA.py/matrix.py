# a = [[1,2],[3,4]]
# b = [[5,6],[7,8]]

# result = [[0,0],[0,0]]

# for i in range(2):
#     for j in range(2):
#         result[i][j] = a[i][j] + b[i][j]

# print(result)
a = [[1,2,3],
     [4,5,6]]

transpose = []

for i in range(len(a[0])):
    row = []

    for j in range(len(a)):
        row.append(a[j][i])

    transpose.append(row)

print(transpose)