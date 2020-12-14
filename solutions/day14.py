import re
import itertools

data_file = open('./data/data14')
data = data_file.read().split('\n')
data_file.close()

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools .combinations(s, r) for r in range(len(s)+1))

def apply_mask(value, mask):
    return (value | int(mask.replace('X', '0'), 2)) & int(mask.replace('X', '1'), 2)

def write_mem(memory, memory_index, memory_value, mask, version):
    if version == 1:
        memory[memory_index] = apply_mask(memory_value, mask)
    elif version == 2:
        power_indexes = [i for (i, char) in enumerate(reversed(mask)) if char == 'X']
        # Apply the mask, set X positions in the mask to 0
        base_index = (memory_index | int(mask.replace('X', '0'), 2)) & int(mask.replace('0', '1').replace('X', '0'), 2)
        for set in powerset(power_indexes):
            mask_value = sum(map(lambda x: 2**x, set))
            memory[base_index + mask_value] = memory_value

def initialize(rows, version):
    memory = {}
    mask = ''
    for row in rows:
        if row.startswith('mask'):
            mask = row.split(' = ')[1]
        elif row.startswith('mem'):
            memory_index = int(re.split('\[|\]', row)[1])
            memory_value = int(row.split(' = ')[1])
            write_mem(memory, memory_index, memory_value, mask, version)
    return memory

print(sum(initialize(data, 1).values()))
print(sum(initialize(data, 2).values()))
