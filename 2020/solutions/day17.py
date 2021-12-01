import numpy as np
import copy

data_file = open('./2020/data/data17')
data = list(map(lambda r: list(map(lambda c: 1 if c == '#' else 0, r)), data_file.read().split('\n')))
data_file.close()

def get_neighbors(grid, x, y, z):
    return grid[z-1:z+2][:, x-1:x+2][:, :, y-1:y+2]

def get_neighbors_4d(grid, x, y, z, w):
    return grid[z-1:z+2][:, x-1:x+2][:, :, y-1:y+2][:, :, :, w-1:w+2]

def apply_cycle(grid_input):
    grid_input = np.array(np.pad(grid_input, 1))
    grid_updated = copy.deepcopy(grid_input)

    for z, layer in enumerate(grid_input[1:-1], 1):
        for x, row in enumerate(layer[1:-1], 1):
            for y, value in enumerate(row[1:-1], 1):
                neighbors = get_neighbors(grid_input, x, y, z)
                neighbors_sum = sum(np.ravel(neighbors)) - value
                if value and (neighbors_sum != 2 and neighbors_sum != 3):
                    grid_updated[z][x][y] = 0
                elif not value and neighbors_sum == 3:
                    grid_updated[z][x][y] = 1
    return grid_updated

def apply_cycle_4d(grid_input):
    grid_input = np.array(np.pad(grid_input, 1))
    grid_updated = copy.deepcopy(grid_input)

    for z, layer in enumerate(grid_input[1:-1], 1):
        for x, row in enumerate(layer[1:-1], 1):
            for y, column in enumerate(row[1:-1], 1):
                for w, value in enumerate(column[1:-1], 1):
                    neighbors = get_neighbors_4d(grid_input, x, y, z, w)
                    neighbors_sum = sum(np.ravel(neighbors)) - value
                    if value and (neighbors_sum != 2 and neighbors_sum != 3):
                        grid_updated[z][x][y][w] = 0
                    elif not value and neighbors_sum == 3:
                        grid_updated[z][x][y][w] = 1
    return grid_updated


grid_3d = np.pad([data], 1)
grid_4d = np.pad([[data]], 1)

for cycle in range(6):
    grid_3d = apply_cycle(grid_3d)
    grid_4d = apply_cycle_4d(grid_4d)

print(sum(np.ravel(grid_3d)))
print(sum(np.ravel(grid_4d)))
