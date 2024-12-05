##fileName = "example.txt"
fileName = "input.txt"

def search_horizontal(grid, i, j):
    total = 0
    max_col = len(grid[i])
    # forwards
    if (j + 3 < max_col):
        if grid[i][j+1] == 'M' and grid[i][j+2] == 'A' and grid[i][j+3] == 'S':
            total += 1
    # backwards
    if (j - 3 >= 0):
        if grid[i][j-1] == 'M' and grid[i][j-2] == 'A' and grid[i][j-3] == 'S':
            total += 1
    return total

def search_vertical(grid, i, j):
    total = 0
    max_row = len(grid)
    # down
    if (i + 3 < max_row):
        if grid[i+1][j] == 'M' and grid[i+2][j] == 'A' and grid[i+3][j] == 'S':
            total += 1
    # up
    if (i - 3 >= 0):
        if grid[i-1][j] == 'M' and grid[i-2][j] == 'A' and grid[i-3][j] == 'S':
            total += 1
    return total     

def search_diagonal(grid, i, j):
    total = 0
    max_col = len(grid[i])
    max_row = len(grid)
    # northwest
    if (j - 3 >= 0 and i - 3 >= 0):
        if grid[i-1][j-1] == 'M' and grid[i-2][j-2] == 'A' and grid[i-3][j-3] == 'S':
            total += 1
    # northeast
    if (j + 3 < max_col and i - 3 >= 0):
        if grid[i-1][j+1] == 'M' and grid[i-2][j+2] == 'A' and grid[i-3][j+3] == 'S':
            total += 1
    # southwest
    if (j - 3 >= 0 and i + 3 < max_row):
        if grid[i+1][j-1] == 'M' and grid[i+2][j-2] == 'A' and grid[i+3][j-3] == 'S':
            total += 1
    # southeast
    if (j + 3 < max_col and i + 3 < max_row):
        if grid[i+1][j+1] == 'M' and grid[i+2][j+2] == 'A' and grid[i+3][j+3] == 'S':
            total += 1
    return total

grid = []
total = 0

with open(fileName, 'r') as file:
    num_rows = 0
    for line in file:
        line = line.rstrip()
        grid.append(list(line))


num_rows = len(grid)
num_cols = len(grid[0])

for i in range(num_rows):
    for j in range(num_cols):
        if grid[i][j] == 'X':
            total += search_horizontal(grid, i, j)
            total +=  search_vertical(grid, i, j)
            total += search_diagonal(grid, i, j)
            
            
print(total)