grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x = 0
y = 0
for i in range(len(grid) - 1):
    for g in grid:
        print(grid[x][y], end='')
        if x < 8:
            x += 1
        else:
            break
    print()
    x = 0
    y += 1
    if y == 6:
        break

'''
Simpler Solution
for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x],end='')
    print()
'''
