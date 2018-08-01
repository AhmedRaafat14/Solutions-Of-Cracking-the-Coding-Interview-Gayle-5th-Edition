'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row
and column are set to 0.
'''


def change_to_zero(matrix):
    n = len(matrix)
    if n == 0:
        return matrix
    m = len(matrix[0])

    zero_rows = zero_cols = []
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 0:
                zero_rows.append(row)
                zero_cols.append(col)

    for row in range(n):
        for col in range(m):
            if row in zero_rows or col in zero_cols:
                matrix[row][col] = 0

    return matrix


if __name__ == "__main__":
    print( change_to_zero([[1, 2, 3], [4, 0, 5], [6, 7, 8]]) )
    print( change_to_zero([[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]) )
