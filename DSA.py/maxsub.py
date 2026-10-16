
sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

# for i in range(0, 9, 3):
#     for j in range(0, 9, 3):
#         total = 0

#         for r in range(i, i + 3):
#             for c in range(j, j + 3):
#                 total += sudoku[r][c]

#         print("Subgrid sum:", total)

# for col in range(9):
#     column = []

#     for row in range(9):
#         column.append(sudoku[row][col])

#     if len(set(column)) == 9:
#         print("Column", col + 1, "is valid")
#     else:
#         print("Column", col + 1, "is invalid")

for i in range(0, 9, 3):
    for j in range(0, 9, 3):

        values = []

        for r in range(i, i + 3):
            for c in range(j, j + 3):
                values.append(sudoku[r][c])

        if len(set(values)) == 9:
            print("Subgrid", i // 3 + 1, j // 3 + 1, "is valid")
        else:
            print("Subgrid", i // 3 + 1, j // 3 + 1, "is invalid")
