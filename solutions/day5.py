import re
import numpy as np
from itertools import groupby

data_file = open('./data/data5')
data = list(data_file.read().split('\n'))
data_file.close()

def parse_row(row_letters):
    row_number = 0
    for index, letter in enumerate(row_letters[::-1]):
        if letter == 'B':
            row_number += 2**index
    return row_number

def parse_column(col_letters):
    col_number = 0
    for index, letter in enumerate(col_letters[::-1]):
        if letter == 'R':
            col_number += 2**index
    return col_number

def parse_seat(seat):
    row = parse_row(list(seat[0:7]))
    column = parse_column(list(seat[7:10]))
    id = row*8+column
    return [row, column, id]

# 1
seats = np.array(list(map(parse_seat, data)))
max_id = max(seats[:,2])
print('Max id: {0}'.format(max_id))

# 2
def find_my_row(seat_rows):
    for row in range(0, 128):
        if row > 7 and row < 109:
            if (list(seat_rows).count(row) < 8):
                return row

def find_my_col(seats):
    for col in range(0, 8):
        if (not list(filter(lambda seat: seat[1] == col, seats))):
            return col

my_row = find_my_row(seats[:,0])
my_col = find_my_col(list(filter(lambda seat: seat[0] == my_row, seats)))
my_id = my_row*8+my_col

print('My id: {0}'.format(my_id))