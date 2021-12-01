with open('./2020/data/data03') as data_file:
    data = list(data_file.read().split())

def check_trees(grid, x, y, x_step, y_step):
    trees_encountered = 0
    while y < len(grid):
        trees_encountered += grid[y][x % len(grid[0])] == "#"
        x += x_step
        y += y_step
    return trees_encountered

# 3.1
print(check_trees(data, 0, 0, 3, 1))

# 3.2
a = check_trees(data, 0, 0, 1, 1)
b = check_trees(data, 0, 0, 3, 1)
c = check_trees(data, 0, 0, 5, 1)
d = check_trees(data, 0, 0, 7, 1)
e = check_trees(data, 0, 0, 1, 2)

print(a*b*c*d*e)