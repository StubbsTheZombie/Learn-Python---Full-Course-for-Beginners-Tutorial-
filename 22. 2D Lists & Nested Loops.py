
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#four rows three columns

print(number_grid[0][0])
print(number_grid[0][1])
print(number_grid[0][2])
print(number_grid[1][0])
print(number_grid[1][1])
print(number_grid[1][2])
print(number_grid[2][0])
print(number_grid[2][1])
print(number_grid[2][2])
print(number_grid[3][0])

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)