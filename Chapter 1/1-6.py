'''
Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
place?
'''


def rotate_matrix(m):
    n = len(m)
    rotated_m = [None] * n
    for r in range(n):
        rotated_m[r] = [None] * n

    for row in range(n):
        for col in range(n):
            rotated_m[n - col - 1][row] = m[row][col]

    return rotated_m

def rotate_matrix_in_place(m):
  n = len(m)

  for col in range(n//2):
    for row in range(col, n - col - 1):
      temp1 = m[n - col - 1][row]
      m[n - col - 1][row] = m[row][col]

      temp2 = m[n - row - 1][n - col - 1]
      m[n - row - 1][n - col - 1] = temp1

      temp1 = m[col][n - row - 1]
      m[col][n - row - 1] = temp2
      m[row][col] = temp1

  return m


if __name__ == "__main__":
    print(rotate_matrix([[1, 2], [3, 4]]))
    print(rotate_matrix_in_place([[1, 2], [3, 4]]))
