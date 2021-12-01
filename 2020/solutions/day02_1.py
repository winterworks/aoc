import re
import numpy as np

with open('./2020/data/data02') as data_file:
    data = np.array(re.split(' |-|:|\n', data_file.read()))
data = data.reshape(-1, 5)
data = np.delete(data, 3, 1)

valid_passwords = 0

for row in data:
    count = len(re.findall(row[2], row[3]))
    if count >= int(row[0]) and count <= int(row[1]):
        valid_passwords += 1

print(valid_passwords)