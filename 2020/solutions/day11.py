import numpy as np
from scipy import signal
import math

data_file = open('./2020/data/data11')
data = np.array(list(map(lambda row: list(row), data_file.read().split('\n'))))
data_file.close()

# Use numers for easier proccesing
data = np.where(data == 'L', 2, data)
data = np.where(data == '#', 1, data)
data = np.where(data == '.', 0, data)
data = np.array(data, dtype=int)
# Save the seat locations, in case anybody sits on the ground
seat_locations = np.where(data == 2, 1, data)
rows_s = np.where(data == 2, 0, data)
rows_a = np.where(data == 2, 0, data)

def apply_simple_rules(rows, seat_locations):
    counts = signal.convolve2d(rows, np.ones((3,3)), mode='same')
    rows = rows + np.where(counts == 0, 1, 0)
    rows = rows * np.where(counts > 4, 0, 1)
    rows = rows * seat_locations
    return rows

def first_encounter(array, values):
    for value in array:
        if value in values:
            return value
    return 0

# Variable names if for the directions there is a seat occupied
# nw n ne
#   \|/
# w--*--e
#   /|\
# sw s se
def get_derection_columns(rows, row, row_i, col_i):
    half_index = len(rows[0])/2-0.5
    distance_to_median = col_i - half_index
    reverse_col_i = math.floor(half_index-distance_to_median)
    distance_to_side = min([row_i, col_i])
    reverse_distance_to_side = min([row_i, reverse_col_i])

    w = np.flip(row[:col_i])
    e = row[col_i+1:]
    n = np.flip(rows[:row_i,col_i])
    s = rows[row_i+1:,col_i]
    nw = np.flip(np.diag(rows, col_i-row_i)[:distance_to_side])
    se = np.diag(rows, col_i-row_i)[distance_to_side+1:]
    ne = np.flip(np.diag(np.fliplr(rows), reverse_col_i-row_i)[:reverse_distance_to_side])
    sw = np.diag(np.fliplr(rows), reverse_col_i-row_i)[reverse_distance_to_side+1:]

    return [w,e,n,s,nw,se,ne,sw]

def apply_advanced_rules(rows, seat_locations):
    counts = np.empty(rows.shape)
    rows = rows + seat_locations
    for row_i, row in enumerate(rows):
        for col_i, cell in enumerate(row):
            derection_columns = get_derection_columns(rows, row, row_i, col_i)
            counts[row_i][col_i] = sum(map(lambda col: 2 == first_encounter(col, [1,2]), derection_columns))

    rows = rows - seat_locations
    rows = rows + np.where(counts == 0, 1, 0)
    rows = rows * np.where(counts > 4, 0, 1)
    rows = rows * seat_locations
    rows = np.where(rows > 1, 1, rows)
    return rows

# Calculate the first answer
new_s_rows = apply_simple_rules(rows_s, seat_locations)
while not np.array_equal(rows_s, new_s_rows):
    rows_s = new_s_rows
    new_s_rows = apply_simple_rules(rows_s, seat_locations)
print(sum(sum(new_s_rows)))

# Calculate the second answer
new_a_rows = apply_advanced_rules(rows_a, seat_locations)
while not np.array_equal(rows_a, new_a_rows):
    rows_a = new_a_rows
    new_a_rows = apply_advanced_rules(rows_a, seat_locations)
print(sum(sum(new_a_rows)))