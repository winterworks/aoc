with open('./2021/data/data02') as data_file:
    data = data_file.read().split('\n')

# First answer
h = d = 0
for command in data:
    [dir, value] = command.split(' ')
    if (dir == 'forward'):
        h += int(value)
    elif (dir == 'down'):
        d += int(value)
    elif (dir == 'up'):
        d -= int(value)

print(h * d)

# Second answer
h = d = aim = 0
for command in data:
    [dir, value] = command.split(' ')
    if (dir == 'forward'):
        h += int(value)
        d += aim * int(value)
    elif (dir == 'down'):
        aim += int(value)
    elif (dir == 'up'):
        aim -= int(value)

print(h * d)
