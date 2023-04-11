import numpy as np


def find_cover(matrix, x, y, d, visited):
    if d < 0:
        return
    if 0 <= x < matrix.shape[0] and 0 <= y < matrix.shape[0] and not visited[x][y]:
        matrix[x][y] += 1
        visited[x][y] = True
    find_cover(matrix, x + 1, y, d - 1, visited)
    find_cover(matrix, x - 1, y, d - 1, visited)
    find_cover(matrix, x, y + 1, d - 1, visited)
    find_cover(matrix, x, y - 1, d - 1, visited)


n = int(input("Enter the number of blocks: "))
m = int(input("Enter the number of pizzerias: "))
adjacency_matrix = np.zeros((n, n))
print(adjacency_matrix)
for i in range(m):
    x, y, R = input("Enter two block numbers [a, b] and the maximum distance R:").split()
    x = int(x)
    y = int(y)
    R = int(R)
    find_cover(adjacency_matrix, x, y, R, np.full((n, n), False))
print(adjacency_matrix)
print("Maximum overlap: ", np.max(adjacency_matrix))
