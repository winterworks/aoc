import re
import numpy as np

with open('./data/data2') as data_file:
    data = np.array(re.split(' |-|:|\n', data_file.read()))
data = data.reshape(-1, 5)
data = np.delete(data, 3, 1)

valid_passwords = 0

for row in data:
    char1 = row[3][int(row[0])-1] == row[2]
    char2 = row[3][int(row[1])-1] == row[2]
    if char1 ^ char2:
        valid_passwords += 1

print(valid_passwords)