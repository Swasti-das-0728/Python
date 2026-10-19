
# sudoku = [
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]

# # for i in range(0, 9, 3):
# #     for j in range(0, 9, 3):
# #         total = 0

# #         for r in range(i, i + 3):
# #             for c in range(j, j + 3):
# #                 total += sudoku[r][c]

# #         print("Subgrid sum:", total)

# # for col in range(9):
# #     column = []

# #     for row in range(9):
# #         column.append(sudoku[row][col])

# #     if len(set(column)) == 9:
# #         print("Column", col + 1, "is valid")
# #     else:
# #         print("Column", col + 1, "is invalid")

# # for i in range(0, 9, 3):
# #     for j in range(0, 9, 3):

# #         values = []

# #         for r in range(i, i + 3):
# #             for c in range(j, j + 3):
# #                 values.append(sudoku[r][c])

# #         if len(set(values)) == 9:
# # #             print("Subgrid", i // 3 + 1, j // 3 + 1, "is valid")
# # #         else:
# # #             print("Subgrid", i // 3 + 1, j // 3 + 1, "is invalid")


# # # for i in range(9):
# # #     if len(set(sudoku[i])) == 9:
# # #         print("Row", i + 1, "is valid")
# # #     else:
# # #         print("Row", i + 1, "is invalid")


# # def is_valid_sudoku(board):
# #     for i in range(9):
# #         row = [x for x in board[i] if x != 0]
# #         col = [board[r][i] for r in range(9)
# #                if board[r][i] != 0]

# #         if len(row) != len(set(row)):
# #             return False

# #         if len(col) != len(set(col)):
# #             return False

# #     for r in range(0, 9, 3):
# #         for c in range(0, 9, 3):
# #             box = []

# #             for i in range(r, r + 3):
# #                 for j in range(c, c + 3):
# #                     if board[i][j] != 0:
# #                         box.append(board[i][j])

# # #             if len(box) != len(set(box)):
# # #                 return False

# # #     return True


# # # board = [
# # #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
# # #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
# # #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
# # #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
# # #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
# # #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
# # #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
# # #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
# # #     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# # # ]

# # # print("Valid Sudoku!" if is_valid_sudoku(board)
# # #       else "Invalid Sudoku!")


# # board = [
# #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
# #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
# #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
# #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
# #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
# #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
# #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
# #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
# #     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# # ]

# # empty_cells = []

# # for r in range(9):
# #     for c in range(9):
# #         if board[r][c] == 0:
# #             empty_cells.append((r, c))

# # print("Total empty cells:", len(empty_cells))
# # print("Empty cell positions (row, column):")

# # for cell in empty_cells:
# #     print(cell)


# # def candidates(board, row, col):
# #     if board[row][col] != 0:
# #         return []

# #     used = set(board[row])

# #     for r in range(9):
# #         used.add(board[r][col])

# #     start_r = (row // 3) * 3
# #     start_c = (col // 3) * 3

# #     for r in range(start_r, start_r + 3):
# #         for c in range(start_c, start_c + 3):
# #             used.add(board[r][c])

# #     return [n for n in range(1, 10) if n not in used]


# # board = [
# #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
# #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
# #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
# #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
# #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
# #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
# #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
# #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
# #     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# # ]

# # print("Candidates:", candidates(board, 0, 2))


# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

# frequency = {n: 0 for n in range(1, 10)}
# empty = 0

# for row in board:
#     for num in row:
#         if num == 0:
#             empty += 1
#         elif 1 <= num <= 9:
#             frequency[num] += 1

# print("Number frequencies:")

# for num, count in frequency.items():
#     print(f"{num}: {count}")

# print("Empty cells:", empty)


def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None


def valid(board, num, row, col):
    if num in board[row]:
        return False

    for r in range(9):
        if board[r][col] == num:
            return False

    start_r = (row // 3) * 3
    start_c = (col // 3) * 3

    for r in range(start_r, start_r + 3):
        for c in range(start_c, start_c + 3):
            if board[r][c] == num:
                return False

    return True


def solve(board):
    empty = find_empty(board)

    if empty is None:
        return True

    row, col = empty

    for num in range(1, 10):
        if valid(board, num, row, col):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve(board):
    for row in board:
        print(*row)
else:
    print("No solution exists")
