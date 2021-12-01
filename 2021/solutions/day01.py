import numpy as np

# First answer
with open('./2021/data/data01') as data_file:
    data = np.array(list(map(int, data_file.read().split('\n'))))

is_bigger = [index > 0 and number > data[index-1] for index, number in enumerate(data)]
print (is_bigger.count(True))

# Second answer
is_bigger_trio = []
for index, number in enumerate(data):
    if (index > 0 and index < len(data) - 2):
        is_bigger_trio.append(sum(data[index-1:index+2]) < sum(data[index:index+3]))

print (is_bigger_trio.count(True))