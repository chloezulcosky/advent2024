##fileName = "example.txt"
fileName = "input.txt"

def search_for_x(grid, i, j):
    max_col = len(grid[i])
    max_row = len(grid)

    if(i - 1 < 0 or i + 1 >= max_row):
        return False
    if(j - 1 < 0 or j + 1 >= max_col):
        return False

    # directions
    nw = grid[i-1][j-1]
    ne = grid[i-1][j+1]
    sw = grid[i+1][j-1]
    se = grid[i+1][j+1]
    results = [nw, ne, sw, se]
    if(results.count('M') != 2 or results.count('S') != 2):
        return False
    return nw != se


grid = []
with open(fileName, 'r') as file:
    num_rows = 0
    for line in file:
        line = line.rstrip()
        grid.append(list(line))


num_rows = len(grid)
num_cols = len(grid[0])
total = 0
for i in range(num_rows):
    for j in range(num_cols):
        if grid[i][j] == 'A':
            if(search_for_x(grid, i, j)):
                total += 1
            
            
print(total)